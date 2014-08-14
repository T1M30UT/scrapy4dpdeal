#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from dp.items import DpItem


class DpSpider(CrawlSpider):
    name = 'dpspider'
    start_urls = ['http://t.dianping.com/citylist']
    rules = [
        Rule(LinkExtractor(allow_domains = ['t.dianping.com'],allow=['/c/', 'pageno='], deny=['desc', 'sort', 'item', '/hotel/', '/goods/', ], ), ),
        Rule(LinkExtractor(allow_domains = ['t.dianping.com'],allow='/deal/', ), callback='parse_item'),
    ]


    def parse_item(self, response):

        d = {}
        if response.status == 200:
            text = response.xpath("//script[contains(.,'dealGroupId')]").extract()
            if len(text)>0:
                text = text[0].replace('\t', '').replace('\n', '').\
                    replace(' ', '').split("DP.data({")[1].split("});DP.require")[0].replace("\"", "").replace("'", "").split(",")
                for textpair in text:
                    d[textpair.split(":", 1)[0]] = textpair.split(":", 1)[-1]
                item = DpItem()
                item['dealGroupId'] = d.get('dealGroupId', -1)
                item['brandName'] = d.get('brandName', -1)
                item['discussCss'] = d.get('discussCss', -1)
                item['position'] = d.get('position', -1)
                item['channelId'] = d.get('channelId', -1)
                item['klykVersion'] = d.get('klykVersion', -1)
                item['preview'] = d.get('preview', -1)
                item['endDate'] = d.get('endDate', -1)
                item['beginDate'] = d.get('beginDate', -1)
                item['endTimestamp'] = d.get('endTimestamp', -1)
                item['currentTimestamp'] = d.get('currentTimestamp', -1)
                item['minPerUser'] = d.get('minPerUser', -1)
                item['maxPerUser'] = d.get('maxPerUser', -1)
                item['isCard'] = d.get('isCard', -1)
                item['isLottery'] = d.get('isLottery', -1)
                item['staticSwitch'] = d.get('staticSwitch', -1)
                item['shortTitle'] = d.get('shortTitle', -1)
                item['category'] = d.get('category', -1)
                item['subCategory'] = d.get('subCategory', -1)
                item['image'] = d.get('image', -1)
                item['dealGroupDetail'] = d.get('isMultiDeal', -1)
                item['isMultiDeal'] = d.get('isMultiDeal', -1)
                item['delivery'] = d.get('delivery', -1)
                item['price'] = d.get('price', -1)
                return item
            return None
        return None
