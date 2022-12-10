import pathlib
import os
import requests
import asyncio

from telegram import *
# from news import *


class ParserOrganizer():
    '''
    Класс для организации работы парсеров
    '''    
    def __init__(self, telegramm_config) -> None:
        self.telegramParser = TelegramParser(telegramm_config)

    def setChannels(self, channels: list):
        self.telegramParser.setChannels(channels)

    def setSearchQuery(self, search_query):
        self.telegramParser.setSearchQuery(search_query)

    def setTimeBorders(self, from_date: datetime.date, to_date: datetime.date):
        self.telegramParser.setTimeBorders(from_date, to_date)

    async def run(self) -> list:
        return await self.telegramParser.run()
        
path = pathlib.Path(__file__).resolve().parent
organizer = ParserOrganizer(os.path.join(path, 'TELETHONE.env'))
organizer.setChannels(['https://t.me/insiderUKR'])
organizer.setSearchQuery(['поставки', 'доставки', 'вооружение'])
organizer.setTimeBorders(datetime.date(2022, 12, 1), datetime.date(2022, 12, 10))

data = asyncio.run(organizer.run())

print(data)
# requests.post('http://127.0.0.1:8000/main/addNews/', data={'news':'awwaw', 'orgs':'org', 'locs':'loc'})