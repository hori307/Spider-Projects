# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import pymongo
# from scrapy.conf import settings
import codecs
import json

class DoubanPipeline(object):
    def __init__(self):
        self.file = codecs.open('top250.json', 'w', encoding="utf-8")

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(content)
        return item

    def close_spider(self, spider):
        self.file.close()

    # def __init__(self):
    #     host = settings["MONGODB_HOST"]
    #     port = settings["MONGODB_PORT"]
    #     dbname = settings["MONGODB_DBNAME"]
    #     sheetname= settings["MONGODB_SHEETNAME"]
    #
    #     # 创建MONGODB数据库链接
    #     client = pymongo.MongoClient(host = host, port = port)
    #     # 指定数据库
    #     mydb = client[dbname]
    #     # 存放数据的数据库表名
    #     self.sheet = mydb[sheetname]
    #
    # def process_item(self, item, spider):
    #     data = dict(item)
    #     self.sheet.insert(data)
    #     return item
