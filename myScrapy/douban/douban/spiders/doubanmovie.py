# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubamovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["movie.douban.com"]

    offset = 0
    url = "https://movie.douban.com/top250?start="
    start_urls = (
            url+str(offset),
    )

    def parse(self, response):
        movies = response.xpath("//div[@class='info']")
        for each in movies:
            item = DoubanItem()
            # 标题
            item['title'] = each.xpath(".//span[@class='title'][1]/text()").extract()[0]
            # 评分
            item['star'] = each.xpath(".//div[@class='star']/span[@class='rating_num']/text()").extract()[0]
            yield item

        if self.offset < 225:
            self.offset += 25
            yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
