# -*- coding: utf-8 -*-
import scrapy


class JiaoyiSpider(scrapy.Spider):
    name = 'jiaoyi'
    allowed_domains = ['sse.net.cn']
    urls = 'http://www1.sse.net.cn/newfiling/NVOCC.jsp?PG=&pageno={pageno}&searchText='

    def start_requests(self):
        for i in range(1, 29):
            yield scrapy.Request(url=self.urls.format(pageno=i), callback=self.parse)

    def parse(self, response):
        resluts = response.xpath('//*[@id="openpricetable"]/tr[1]/following-sibling::tr')
        for node in resluts:
            item = {}
            item['中文全称'] = node.xpath('./td[1]/text()').extract()[0]
            item['英文简称'] = node.xpath('./td[2]/text()').extract()[0]
            item['证书号'] = node.xpath('./td[3]/text()').extract_first()
            item['证书有效期'] = node.xpath('./td[4]/text()').extract_first()
            item['责任保证'] = node.xpath('./td[5]/text()').extract_first()
            item['运价幅度'] = node.xpath('./td[6]/a/text()').extract_first()
            item['公布运价'] = node.xpath('./td[7]/a/text()').extract_first()
            yield item

