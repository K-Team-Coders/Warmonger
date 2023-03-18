import json
import datetime
import os

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
    
    def start_requests(self):
        self.connection = psycopg2.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            dbname=DBNAME
        )
        self.rubbish = ["policy", "instagram", "terms", "footer", "download", "service", "youtube", "login", "pdf", "img", "png", "sign", "support", "logout","faq", "blog", "develop","javascript", "accounts", "auth", "user", "forum", "contacts", "facebook", "#page", "cart", "tel", "#", "@", "company", "personal", "action"]
        self.cursor = self.connection.cursor()
        self.visited = []
        self.domens = []

        urls = [
            'https://aeromotus.ru/', 
            "https://nelk.ru/", 
            "https://dji.com/ru/dji-fpv/specs", 
            "https://geobox.ru/"
        ]

        for url in urls:
            left = url.find('//') + 2
            right = url[left:].find('/') + left
            self.domens.append(url[left:right])
            yield scrapy.Request(url=url, method="GET", callback=self.parse)

    def parse(self, response):
        logger.debug(response.url)
        self.visited.append(response.url)
        urls = response.css('a::attr(href)').extract()
        
        cleaned = []
        for url in urls:
            checker = False
            for item in self.rubbish:
                if item in url:
                    checker = True

            domen_checker = False
            for domen in self.domens:
                if domen in url:
                    domen_checker = True
            if not checker and domen_checker:
                cleaned.append(url)

        logger.debug(len(urls))
        logger.debug(len(cleaned))

        logger.debug(cleaned)
        # for url in urls:
            # if url not in self.visited:
                # yield scrapy.Request(url=url, method="GET", callback=self.parse_with_extraction)

    def parse_with_extraction(self, response):
        logger.debug(response.url)
        self.visited.append(response.url)
        urls = response.css('a::attr(href)').extract()
        # logger.debug(urls)

        uls = response.css('ul').extract()
        logger.success(type(uls))
        table = response.xpath('//table').getall()
        logger.success(table)

        for url in urls:
            if url not in self.visited:
                yield scrapy.Request(url=url, method="GET", callback=self.parse_with_extraction)

    def closed(self, reason):
        logger.error(len(self.visited))