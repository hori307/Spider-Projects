# -*- coding: utf-8 -*-

import redis
import pymysql
import json

def main():
    # 指定redis数据库信息
    rediscli = redis.StrictRedis(host='127.0.0.1', port = 6379, db = 0)
    # 指定mysql数据库
    mysqlcli = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db = 'sina', port=3306, use_unicode=True, charset="utf8")

    while True:
        # FIFO模式(先进先出)为 blpop，LIFO模式(先进后出)为 brpop，获取键值
        source, data = rediscli.blpop(["sinaspider:items"])
        # 转为python字典形式
        item = json.loads(data)

        try:
            # 使用cursor()方法获取操作游标
            cur = mysqlcli.cursor()
            # 使用execute方法执行SQL INSERT语句
            cur.execute("insert into sinaInfo(parentTitle, parentUrls, subTitle, subUrls, subFile, sonUrls, head, content) values(%s, %s, %s, %s, %s, %s, %s, %s)",[item['parentTitle'], item['parentUrls'], item['subTitle'], item['subUrls'], item['subFilename'], item['sonUrls'], item['head'], item['content']])
            # 提交sql事务
            mysqlcli.commit()
            #关闭本次操作
            cur.close()
        except pymysql.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

if __name__ == '__main__':
    main()