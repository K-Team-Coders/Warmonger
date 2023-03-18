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
        self.cursor = self.connection.cursor()
        self.visited = []

        urls = [
            'https://aeromotus.ru/', 
            "https://nelk.ru", 
            "https://dji.com/ru/dji-fpv/specs", 
            "https://geobox.ru"
        ]

        for url in urls:
            yield scrapy.Request(url=url, method="GET", callback=self.parse)

    def parse(self, response):
        self.visited.append(response.url)
        urls = response.css('a::attr(href)').extract()
        logger.debug(urls)
        
        for url in urls:
            if url not in self.visited:
                yield scrapy.Request(url=url, method="GET", callback=self.parse_with_extraction)

    def parse_with_extraction(self, response):
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