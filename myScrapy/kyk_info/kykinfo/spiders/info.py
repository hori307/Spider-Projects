# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from kykinfo.items import KykinfoItem

class InfoSpider(CrawlSpider):
    name = 'info'
    allowed_domains = ['keyakizaka46.com']
    start_urls = ['http://www.keyakizaka46.com/s/k46o/search/artist?ima=0000']

    rules = (
        Rule(LinkExtractor(allow=r'/artist/\d+?'), callback='parse_item'),
    )

    def parse_item(self, response):
        item = KykinfoItem()
        item['name'] = response.xpath('//div[@class="box-profile_text"]/p[2]/text()').extract()[0].strip()
        item['birthday'] = response.xpath('//div[@class="box-info"]/dl[1]/dt/text()').extract()[0].strip()
        item['constellation'] = response.xpath('//div[@class="box-info"]/dl[2]/dt/text()').extract()[0].strip()
        item['height'] = response.xpath('//div[@class="box-info"]/dl[3]/dt/text()').extract()[0].strip()
        item['birthplace'] = response.xpath('//div[@class="box-info"]/dl[4]/dt/text()').extract()[0].strip()
        item['bloodType'] = response.xpath('//div[@class="box-info"]/dl[5]/dt/text()').extract()[0].strip()
        yield  item


