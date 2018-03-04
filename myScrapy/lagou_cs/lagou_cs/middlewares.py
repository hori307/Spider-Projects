#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
from settings import USER_AGENTS
from settings import PROXIES

class RandomUserAgent(object):
    def process_request(self, request, spider):
        useragent = random.choice(USER_AGENTS)
        request.headers.setdefault("User-Agent", useragent)

class RandomProxy(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        request.meta['proxy'] = "http://" + proxy['ip_port']