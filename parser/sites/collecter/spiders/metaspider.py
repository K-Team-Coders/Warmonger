import json
import datetime
import os
import random

from bs4 import BeautifulSoup as BS
import psycopg2
import scrapy
from loguru import logger
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(os.path.join(Path(__file__).resolve().parent.parent.parent.parent.parent, 'DB.env'))

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DBNAME = os.getenv("DBNAME")

class MetaSpider(scrapy.Spider):
    name = "metaspider"
    
    def preprocessing_urls(self, urls):
        """
        Предобработка ссылок 
        """
        cleaned = []
        for url in urls:
        
            if len(url) > 0:

                # Нахождение ненужных юрлов по типу контакты, форумы и т.п.
                checker = False
                for item in self.rubbish:
                    if item in url:
                        checker = True      

                # Чек на вложенные запросы
                if url[0] == '/':
                    cleaned.append("https://" + str(self.current_domen) + str(url))
                    break

                # Проверка на нахождение в том же домене (против бесконечных блужданий по интернету)
                domen_checker = False
                if self.current_domen in url:
                    domen_checker = True

                # Финальный чек и проверка на PHP-производные сайты
                if not checker and domen_checker:
                    cleaned.append(url)

        return cleaned

    def start_requests(self):
        self.connection = psycopg2.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            dbname=DBNAME
        )
        self.rubbish = ["policy", "instagram", "wp-content", "terms", "webinar", "footer", "download", "service", "youtube", "login", "pdf", "jpeg", "img", "jpg", "png", "sign", "support", "logout","faq", "blog", "develop","javascript", "accounts", "auth", "user", "forum", "contacts", "facebook", "#page", "cart", "tel", "@", "company", "personal", "action"]
        self.cursor = self.connection.cursor()
        self.current_domen = ''

        self.visited = []
        self.sitemap = []

        self.headers = []

        with open(os.path.join(Path.cwd().joinpath('collecter').joinpath('spiders'), 'agents.json')) as f:
            self.headers = json.load(f)
        
        urls = [
            # 'https://aeromotus.ru/product/dji-matrice-30t/',
            # 'https://aeromotus.ru/webinar/dji-mavic-3-seriya-enterprise/',
            # 'https://aeromotus.ru/', 
            # "https://nelk.ru/", 
            # "https://dji.com/", 
            "https://geobox.ru/"
        ]

        for url in urls:
            left = url.find('//') + 2
            right = url[left:].find('/') + left
            self.current_domen = url[left:right]
            yield scrapy.Request(url=url, method="GET", callback=self.parse)

    def parse(self, response):
        logger.debug(response.url)
        for item in self.rubbish:
            if item in response.url:
                logger.debug('Filter error')
                yield None
        self.visited.append(response.url)
        logger.debug(len(self.sitemap))
        logger.debug(len(self.visited))
        
        try:
            # Добавление юрлов
            body = response.xpath('//div')
            urls = body.css('a::attr(href)').extract()
            cleaned = self.preprocessing_urls(urls)
            self.sitemap.extend(cleaned)
            self.sitemap = list(set(self.sitemap))

            # Обработка текста
            soup = BS(response.text, 'html.parser')
            # # Нашли слово характеристики
            params = soup.find(text='Характеристики')
            if params:
                # Если нашли в ссылке - продолжаем парсинг
                try:
                    href = params.parent.parent.find('a').get('href')
                    header = {
                        "User-Agent": self.headers[random.randrange(0, len(self.headers))]["user_agent"]
                    }

                    # Если PHP - стиль
                    if href[0] == '/':
                        link = "https://" +self.current_domen + href
                        logger.success(link)
                        yield scrapy.Request(url=link, method="GET", headers=header, callback=self.parse)

                    # Если стандартный переход 
                    else:
                        logger.success(href)
                        yield scrapy.Request(url=href, method="GET", headers=header, callback=self.parse)
                except Exception as e:
                    logger.error(e)
                except:
                    logger.error('Not a href inside!')

                # Если ссылки нет значит проверяем ближайшие тэги
                
                logger.warning(params.parent.parent)

            # Не нашли характеристики? https://i.pinimg.com/originals/01/e6/c2/01e6c2368a9720c63ac7a981c4500302.png
            # Ищем дальше по тому что есть 
            else:
                for url in cleaned:
                    if url not in self.visited:
                        header = {
                            "User-Agent": self.headers[random.randrange(0, len(self.headers))]["user_agent"]
                        }
                        yield scrapy.Request(url=url, method="GET", headers=header, callback=self.parse)
        except Exception as e:
            logger.error(e)
        
        
    # def parse_full_urls(self, response):
    #     logger.debug(response.url)
    #     self.visited.append(response.url)
    #     urls = response.css('a::attr(href)').extract()
        
    #     cleaned = self.preprocessing_urls(urls)

        

    # def parse_with_extraction(self, response):
    #     logger.debug(response.url)
    #     self.visited.append(response.url)
    #     urls = response.css('a::attr(href)').extract()

    #     uls = response.css('ul').extract()
    #     logger.success(type(uls))
    #     table = response.xpath('//table').getall()
    #     logger.success(table)

    #     for url in urls:
    #         if url not in self.visited:
    #             yield scrapy.Request(url=url, method="GET", callback=self.parse_with_extraction)

    def closed(self, reason):
        logger.success(f"Crawled {len(self.visited)}")
        logger.success(f"Total {len(self.sitemap)}")