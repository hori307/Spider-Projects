# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class KykinfoItem(scrapy.Item):
    name = scrapy.Field()
    birthday = scrapy.Field()
    constellation = scrapy.Field()
    height = scrapy.Field()
    birthplace = scrapy.Field()
    bloodType = scrapy.Field()

