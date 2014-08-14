# -*- coding: utf-8 -*-

from scrapy import log
from scrapy.conf import settings
from scrapy.http import Request
import random


class CachedMiddleware(object):

    def process_spider_output(self, response, result, spider):
        proxy_list = settings.get('PROXY_LIST')
        proxy = random.choice(proxy_list)

        if (response.status == 403):
            request_with_cached_url = Request(response.url,meta={'proxy': proxy})
            result = [request_with_cached_url,]
            return result
        else:
            return result
