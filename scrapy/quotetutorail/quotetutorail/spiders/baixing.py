# -*- coding: utf-8 -*-
import scrapy
import re

class BaixingSpider(scrapy.Spider):
    name = 'baixing'
    allowed_domains = ['baixing.com']
    start_urls = ['http://chongqing.baixing.com/baomu/?page=1']

    def parse(self, response):

        item = {}
        node_list = response.xpath('//*[@class="contact-button"]/@data-contact').extract()
        for node in node_list:
            item['phone'] = node
            yield item

        next_page = response.xpath('//li[contains(./a/text(),"下一页")]/a/@href').extract_first()
        if next_page:
            next_page = response.urljoin(next_page)
            if next_page.startswith('http://chongqing.baixing.com/oz/s9verif'):
                page = re.search('redirect=(.*)', next_page, re.S).group(1).encode('utf-8')
                print(page)
                yield scrapy.Request(url=page, callback=self.parse)
            else:
                yield scrapy.Request(url=next_page, callback=self.parse)

