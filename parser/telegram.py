import datetime
import re
import os

from tqdm.asyncio import tqdm
from loguru import logger
from telethon import TelegramClient
import nest_asyncio
nest_asyncio.apply()

class TelegramParser():

    def __init__(self, config) -> None:
        '''
        Реквизиты приложения. Согласно документации telethone
        '''
        
        from dotenv import load_dotenv
        load_dotenv(config)

        self.api_id = os.getenv('TELETHONE_ID') 
        self.api_hash = os.getenv('TELETHONE_HASH')
        self.session_name = 'Session'
    
    def setSearchQuery(self, query) -> None:
        '''
        Ключевое слово или слова для поиска
        '''
        if type(query) != type([1,2]):
            self.search_keys = [query]
        else:
            self.search_keys = query

    def setTimeBorders(self, from_date: datetime.date, to_date: datetime.date ) -> None:
        '''
        Диапазон дат (год, месяц, день)
        '''
        self.from_date = from_date
        self.to_date = to_date

    def setChannels(self, channels: list) -> None:
        '''
        Список каналов. Принимаются id, номера телефонов, имена пользователей.
        '''
        self.chat_list = channels

    async def run(self) -> list:
        '''
        По введении параметров - запускаете эту функцию
        '''
        self.client = TelegramClient(self.session_name, self.api_id, self.api_hash)

        result = []
        
        for chat in self.chat_list:
            async def get_messages_at_date(chat, from_date, to_date, search_key):
                result = []
                for key in search_key:
                    limit_day = to_date + datetime.timedelta(days=1)
                    lower_day = from_date - datetime.timedelta(days=1)
                    iterator = self.client.iter_messages(chat, offset_date=limit_day, search=key)
                    async for message in tqdm(iterator):
                        if message.date.day == lower_day.day and message.date.month == lower_day.month and message.date.year == lower_day.year:
                            return result
                        edited_text = re.sub('[^\x00-\x7Fа-яА-Я]', '', message.text)
                        one_message_info = [message.sender.username, message.date, edited_text]
                        result.append(one_message_info)

            async with self.client:
                date_filt = self.client.loop.run_until_complete(get_messages_at_date(chat, self.from_date, self.to_date, self.search_keys))
                if date_filt != None:
                    result.append(date_filt)

        return result