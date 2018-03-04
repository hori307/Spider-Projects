# -*- coding: utf-8 -*-
import scrapy
import json
from bililive.items import BililiveItem

class CoverSpider(scrapy.Spider):
    name = 'cover'
    allowed_domains = ['api.live.bilibili.com']
    url1 = 'https://api.live.bilibili.com/room/v1/Area/getRoomList?access_key=5905896444198da0a018ade7ed83d0e8&actionKey=appkey&appkey=27eb53fc9058f8c3&area_id=0&build=6190&cate_id=0&device=phone&mobi_app=iphone&page='
    page = 1
    url2 = '&parent_area_id=1&platform=ios&sign=df8e434762e38923b4e9889647b9ea79&sort_type=online&ts=1519108343'
    start_urls = [url1 + str(page) + url2]

    def parse(self, response):
        data = json.loads(response.text)['data']
        for each in data:
            item = BililiveItem()
            item['uname'] = each['uname']
            item['cover'] = each['user_cover']

            yield item

        # self.page += 1
        # yield scrapy.Request(self.url1 + str(self.page) + self.url2, callback = self.parse)

