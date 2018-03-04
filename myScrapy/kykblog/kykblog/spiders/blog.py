# -*- coding: utf-8 -*-
# 小池美波获取有bug，尚未解决！！！
from kykblog.items import KykblogItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class BlogSpider(CrawlSpider):
    name = 'blog'
    allowed_domains = ['keyakizaka46.com']
    # 选择成员
    # 01：石森虹花  02：今泉佑唯  03：上村莉菜    04：尾関梨香  05：织田奈那  06：小池美波    07：小林由依  08：斋藤冬优花  09：佐藤诗织  10：志田爱佳
    # 11：菅井友香  12：铃本美愉  13：长泽菜菜香  14：土生瑞穗  15：原田葵    17：平手友梨柰  18：守屋茜    19：米谷奈奈未  20：渡边梨加  21：渡边理佐  22：长滨ねる
    ct = '10'
    # 请自行修改 settings.py 中的 IMAGES_STORE ，即图片保存路径
    start_urls = ['http://www.keyakizaka46.com/s/k46o/diary/member/list?ima=0000&page=0&cd=member&ct=' + ct]

    rules = (Rule(LinkExtractor(allow=r'page=\d+'), callback='parse_item', follow=True), )

    def parse_item(self, response):
        # 获取本页所有博客
        blogList = response.xpath('//article')
        # 遍历所有博客
        for each in blogList:
            # 获取本篇博客发送日期
            date = each.xpath('.//div[@class="box-bottom"]/ul/li[1]/text()').extract()[0].strip().replace("/","-").replace(":","-")
            # 获取本篇博客所有图片
            num = 1
            for image_url in each.xpath('.//img[not(@class="emoji") and not(contains(@src,"gif"))]/@src').extract():
                item = KykblogItem()
                item['date'] = date + " - " + str(num)
                item['image_url'] = image_url
                yield item
                num += 1