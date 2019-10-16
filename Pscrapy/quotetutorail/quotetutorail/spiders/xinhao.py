# -*- coding: utf-8 -*-
import scrapy


class XinhaoSpider(scrapy.Spider):
    name = 'xinhao'
    allowed_domains = ['cecb2b.com']
    start_urls = ['http://www.cecb2b.com/icxinghao/1/1.html']

    def parse(self, response):
        node_list = response.xpath('//*[@class="icmodelsel"]/p/font[2]/a')
        for node in node_list:
            href = node.xpath('./@href').extract_first()
            href = response.urljoin(href)
            page = href.replace('index', '1')
            yield scrapy.Request(url=page, callback=self.parse1)


    def parse1(self, response):
        node_list = response.xpath('//*[@class="icmodelresults"]/ul/li')
        for node in node_list:
            item = {}
            item['title'] = node.xpath('./a[1]/text()').extract_first()
            item['href'] = node.xpath('./a[1]/@href').extract_first()
            yield item

        next_page = response.xpath('//span[contains(.//text(),"下一页")]/a/@href').extract_first()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse1)

