import json
import time

import scrapy
from loguru import logger

from ..items import *

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
        th = response.xpath('//table//tr//th/text()').getall()
        td = response.xpath('//table//tr//td/text()').getall()

        for index in range(len(th)):
            logger.success(th[index] + " || " + td[index])