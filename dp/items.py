# -*- coding: utf-8 -*-

import scrapy


class DpItem(scrapy.Item):
    dealGroupId = scrapy.Field()
    brandName = scrapy.Field()
    discussCss = scrapy.Field()
    position = scrapy.Field()
    channelId = scrapy.Field()
    klykVersion = scrapy.Field()
    preview = scrapy.Field()
    endDate = scrapy.Field()
    beginDate = scrapy.Field()
    endTimestamp = scrapy.Field()
    currentTimestamp = scrapy.Field()
    minPerUser = scrapy.Field()
    maxPerUser = scrapy.Field()
    isCard = scrapy.Field()
    isLottery = scrapy.Field()
    staticSwitch = scrapy.Field()
    shortTitle = scrapy.Field()
    category = scrapy.Field()
    subCategory = scrapy.Field()
    image = scrapy.Field()
    dealGroupDetail = scrapy.Field()
    isMultiDeal = scrapy.Field()
    delivery = scrapy.Field()
    price = scrapy.Field()