from pathlib import Path
from loguru import logger

import scrapy

from ..items import CollecterItem

class DronesCnasSpider(scrapy.Spider):
    name = "dronescnas"

    def start_requests(self):
        urls = [
            'https://drones.cnas.org/drones/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        cards = response.xpath('//div[@class="drone-box"]')
        for card in cards:
            data = card.xpath('.//dd/text()').getall()
            item = CollecterItem()
            item["country"] = data[0]
            item["company"] = data[1]
            item["platform"] = data[2]
            item["endurance"] = data[3]
            item["range_"] = data[4].split()[0]
            item["payload"] = data[5].split()[0]
            item["altitude"] = data[6].split()[0]
            item["mass"] = data[7].split()[0]
            item["width"] = data[8].split()[0]
            item["length"] = data[9].split()[0]
            yield item