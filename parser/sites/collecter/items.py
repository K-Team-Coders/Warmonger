# Define here the models for your scraped item
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass
import scrapy

@dataclass
class CollecterItem(scrapy.Item):
    country: str
    company: str
    platform: str
    endurance: float
    range: int
    payload: int
    maxspeed: float
    altitude: int
    mass: float
    width: float
    length: float