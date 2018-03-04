# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from lagou_cs.items import LagouCsItem

class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/zhaopin/Python/1']

    rules = (
        Rule(LinkExtractor(allow=r'Python/\d+/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for each in response.xpath('//ul[@class="item_con_list"]/li'):
            item = LagouCsItem()

            item['positionname'] = each.xpath('./@data-positionname').extract()[0]
            item['company'] = each.xpath('./@data-company').extract()[0]
            item['salary'] = each.xpath('./@data-salary').extract()[0]

            yield item
