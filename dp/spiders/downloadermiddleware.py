# -*- coding: utf-8 -*-

from scrapy import log
from scrapy.conf import settings

import random
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class RotateUserAgentMiddleware(UserAgentMiddleware):

    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        if ua:
            request.headers.setdefault('User-Agent', ua)
            log.msg('Current UA: '+ua, level='INFO')
    user_agent_list = settings.get('UA_LIST_BROWSER')


class ProxyMiddleware(object):

    def process_request(self, request, spider):
        proxy = random.choice(self.proxy_list)
        if proxy:
            request.meta['proxy'] = proxy
            log.msg('Current proxy: '+proxy, level='INFO')

    proxy_list = settings.get('PROXY_LIST')


class CachedMiddleware(object):

    def process_request(self, request, spider):
        if request.url.find('googleusercontent')== -1 :
            new_url = "http://webcache.googleusercontent.com/search?q=cache:"+request.url
            request = request.replace(url = new_url,)
            log.msg(request.url, level='INFO')
            return request
