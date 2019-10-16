# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
# 企业信息item
import scrapy
# import sys
# sys.path.append("F:\SEE\SEE")


class EntItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    name = scrapy.Field()
    address = scrapy.Field()
    tel = scrapy.Field()

    pass