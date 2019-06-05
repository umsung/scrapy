# -*- coding: utf-8 -*-
import scrapy
from lxml import etree

class LiebibaoSpider(scrapy.Spider):
    name = 'liebibao'
    allowed_domains = ['liebiao.com']
    start_urls = ['http://zhengzhou.liebiao.com/shouji/']

    def parse(self, response):
        node_list = response.xpath('//*[@class="subcate"]/a')
        for node in node_list:
            url = node.xpath('./@href').extract_first()
            name = node.xpath('./text()').extract_first()
            yield scrapy.Request(url=url, callback=self.parse2)
            # yield scrapy.Request(url=url, callback=self.parse3)

    def parse2(self, response):
        node_list = response.xpath('//*[@class="region"]/a[1]/following-sibling::a')
        for node in node_list:
            url = node.xpath('./@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse3)

    def parse3(self, response):
        node_list = response.xpath('//*[@class="post clf"]')
        for node in node_list:
            url = node.xpath('./div[1]/div[2]/div[1]/h2/a/@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse4)

    def parse4(self, response):
        item = {}
        resp = etree.HTML(response.body.decode('utf-8'))
        item['tel'] = resp.xpath('//*[contains(./text(),"联系方式")]/@data-phone')
        # item['tel'] = response.xpath('//span[@class="phone"]/text()').extract_first()
        yield item