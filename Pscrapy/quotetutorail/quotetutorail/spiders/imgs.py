# -*- coding: utf-8 -*-
import scrapy
import re
from quotetutorail.items import QuotelItem


class ImgsSpider(scrapy.Spider):
    name = 'imgs'
    allowed_domains = ['pic.netbian.com']
    start_urls = ['http://pic.netbian.com/4kmeinv/index.html']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
#       找到下一页连接
        next_href = response.xpath('//*[@class="page"]/a[contains(./text(),"下一页")]/@href').extract_first()
        if next_href:
            yield scrapy.Request(url=response.urljoin(next_href), callback=self.parse)

        img_list = response.xpath('//*[@class="slist"]/ul/li')
        for img in img_list:
            img_href = img.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=response.urljoin(img_href), callback=self.parse_detail)

    def parse_detail(self, response):
        item = QuotelItem()
        title = response.xpath('//div[@class="photo-hd"]/h1/text()').extract_first()
        img_href = response.xpath('//*[@id="img"]/img/@src').extract_first()
        img_href = response.urljoin(img_href)
        item['title'] = title
        item['img_href'] = img_href
        item['url'] = response.url
        yield item




