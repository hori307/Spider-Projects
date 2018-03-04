# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class LagouItem(scrapy.Item):
    positionname = scrapy.Field()
    company = scrapy.Field()
    salary = scrapy.Field()

