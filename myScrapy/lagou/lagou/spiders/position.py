# -*- coding: utf-8 -*-
import scrapy
from lagou.items import LagouItem

class PositionSpider(scrapy.Spider):
    name = 'position'
    allowed_domains = ['lagou.com']
    url = 'https://www.lagou.com/zhaopin/Python/'
    page = 1
    start_urls = [url+str(page)]

    def parse(self, response):
        for each in response.xpath('//ul[@class="item_con_list"]/li'):
            item = LagouItem()

            item['positionname'] = each.xpath('./@data-positionname').extract()[0]
            item['company'] = each.xpath('./@data-company').extract()[0]
            item['salary'] = each.xpath('./@data-salary').extract()[0]

            yield item

        if self.page < 6:
            self.page += 1

        yield scrapy.Request(self.url+str(self.page), callback = self.parse)