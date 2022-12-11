import pathlib
import os
import requests
import asyncio

from geopy.geocoders import Nominatim
from pymystem3 import Mystem
import spacy

from telegram import *
# from news import *

def lemmatizeText(text: str):
    '''
    Стандартный метод обработки текстов естественного языка
    '''
    mystem = Mystem()
    text_lem = mystem.lemmatize(text)
    tokens = [token for token in text_lem if token != ' ']
    return " ".join(tokens)

def namedEntityRecognition(languageModel, text: str):
    '''
    Вычленение именнованных сущностей
    '''
    # Мусорные отрывки определения сущностей, нужны в целях незахломления базы данных
    rubbish = ['me / joinchat', 'telegram', 'com']
    # Ключевые слова, можете добавлять ЧТО УГОДНО. Хоть сирию, хоть украину, хоть лесные пожары, взрывы и т.п.
    needle = ['поставки', 'вооружение', 'бронетехника', 'авиация', 'техника', 'помошь', 'средства', 'танки', 'оружие']

    lemmtext = lemmatizeText(text)
    k = languageModel(lemmtext)

    locs = []
    orgs = []
    persons = []
    keywords = []

    for i in k.ents:
        check = True
        for x in rubbish:
            if x in i.text:
                check = False
        if check:
            if i.label_ == 'LOC':
                locs.append(i.text)
            if i.label_ == 'ORG':
                orgs.append(i.text)
            if i.label_ == 'PER':
                persons.append(i.text)

    for keyword in needle:
        if keyword in lemmtext:
            keywords.append(keyword)

    locs = list(set(locs))
    orgs = list(set(orgs))
    persons = list(set(persons))
    keywords = list(set(keywords))
    
    return locs, orgs, persons, keywords

class ParserOrganizer():
    '''
    Класс для организации работы парсеров
    '''    
    def __init__(self, telegramm_config) -> None:
        '''
        На входе - конйигурационный файл для работы тг парсера, см. Инструкцию
        '''
        self.telegramParser = TelegramParser(telegramm_config)

        # Можно использовать любую другую языковую модель
        self.ruModel = spacy.load('ru_core_news_sm')
        
        # Геолокатор по названию и населенным пунктам. Позволяет вернуть координаты
        self.loc = Nominatim(user_agent="GetLoc")



    def setChannels(self, channels: list):
        '''
        Установка целевых тг каналов (поддерживается 20+ языков, см. модель spacy)
        Интерфейс предполагает поканальный сбор информации (в перспективе, см интерфейс фильтра поиска)
        '''
        self.telegramParser.setChannels(channels)

    def setSearchQuery(self, search_query: list):
        '''
        Ввод поисковых запросов в формате списка
        Сделано поэлементно в целях избежания утраты информации в случае прерывания.
        '''
        self.searchQuery = search_query

    def setTimeBorders(self, from_date: datetime.date, to_date: datetime.date):
        '''
        Установление границ в формате datetime.date для поиска по тг каналам. 
        Можно доработать до поиска по всему тг каналу, либо по любому удобному формату 
        '''
        self.telegramParser.setTimeBorders(from_date, to_date)

    def defineLocationCoordinates(self, location: str):
        '''
        Установление координат именованных сущностей локации о которой говорится в новости.
        В перспективе возможно дальнейшая доработка до установления любой другой информации, в соответсвии с запросами заказчика
        '''
        getLoc = self.loc.geocode(location)

        adress = getLoc.address
        if len(adress) > 200:
            adress = adress[:199]

        return {
            'name': location,
            'adress': adress,
            'latitude': str(getLoc.latitude),
            'longitude': str(getLoc.longitude)
        }

    def defineLocation(self, location: str):
        '''
        Установление информации о локации (для MVP - координат, в дальнейшем - любые другие источники и темы)
        '''
        return self.defineLocationCoordinates(location)
        

    def defineOrganization(self, organization: str):
        '''
        Установление деятельности организации и другой информации по аналогии с локациями
        '''
        pass

    def definePerson(self, person: str):
        '''
        Установление информации о найденных личностях
        '''
        pass
    
    async def run(self) -> list:
        '''
        Работа тг парсера и надстроек для определния целевых полей в БД, и дальнейшая передача на админку информации о текущей остановке
        '''
        for query in self.searchQuery: 
            self.telegramParser.setSearchQuery(query)
            data = await self.telegramParser.run()
            for chatdata in data:
                for new in chatdata:
                    # Вычленяем из новостей информацию
                    # Source
                    source = 'https://t.me//' + str(new[0])
                    # Date
                    date = new[1]
                    # Text
                    text = new[2]

                    locs, orgs, persons, keywords = namedEntityRecognition(self.ruModel, text)
                    locs = [self.defineLocation(loc) for loc in locs]

                    title = text
                    if len(text) > 50:
                        title = text[:50]                        

                    requests.post('http://127.0.0.1:8000/main/addNews/', json={
                        'title': title,
                        'text': text,
                        'locations': locs,
                        'organizations': orgs,
                        'persons': persons,
                        'date': str(date),
                        'source': source,
                        'keywords': keywords
                    })

path = pathlib.Path(__file__).resolve().parent
organizer = ParserOrganizer(os.path.join(path, 'TELETHONE.env'))
organizer.setChannels(['https://t.me/insiderUKR'])
organizer.setSearchQuery(['вооружение'])
organizer.setTimeBorders(datetime.date(2022, 12, 9), datetime.date(2022, 12, 11))

data = asyncio.run(organizer.run())

# print(data)

# with open('result.txt', 'w') as f:
#     for subdata in data:
#         f.write('\n')
#         for new in subdata:
#             f.write('\n')
#             f.write(str(new))
# requests.post('http://127.0.0.1:8000/main/addNews/', data={'news':'awwaw', 'orgs':'org', 'locs':'loc'})