import json
import time

import scrapy
from loguru import logger

from ..items import Object

class AeromotusSpider(scrapy.Spider):
    name = "aeromotus"

    def start_requests(self):
        urls = ['https://aeromotus.ru/shop/']

        headers = {
            "Content-type": "application/x-www-form-urlencoded"
        }

        for url in urls:
            yield scrapy.Request(url=url, method="POST", body="ppp=-1", headers=headers, callback=self.parse)

    def parse(self, response):
        cards = response.xpath('//div[@class="product-inner product-item__inner"]//a[@class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]/@href')
        urls_ = []
        for card in cards:
            urls_.append(card.get())
        
        data = urls_[:2]
        for url in data:
            yield scrapy.Request(url=url+"#tab-specification", method="GET", callback=self.parse_all_urls)

    def parse_all_urls(self, response):
        name = response.xpath('//h1/text()').get()
        logger.debug(name)


        h3 = response.xpath('//div[@class="woocommerce-Tabs-panel woocommerce-Tabs-panel--specification panel entry-content wc-tab"]//h3/text()').getall()
        logger.debug(h3)

        tables = response.xpath('//table[@class="content_tbl"]')
        for table in tables:
            th = table.xpath('.//tr//th/text()').getall()
            td = table.xpath('.//tr//td/text()').getall()
            logger.debug(th)
