# -*- coding: utf-8 -*-
import scrapy
import json

from scrapy.http import HtmlResponse


class JianshuSpider(scrapy.Spider):
    name = 'jianshu'
    start_urls = []

    def start_requests(self):
        # 爬虫开始时，有且仅执行一次
        for i in range(1, 33):
            self.start_urls.append('https://www.jianshu.com/users/aefb77950a6e/followers?page={}'.format(i))

        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: HtmlResponse):
        """
        http://
        ajx : print(response.body.decode('utf-8'))  获取源代码
        """
        fans_list = response.xpath('//ul[@class="user-list"]//li')
        for fans in fans_list:
            item = {}
            # 粉丝名字
            item['fans_name'] = fans.xpath('./div[@class="info"]/a/text()').extract_first('')
            # 粉丝数量
            item['fans_sum'] = fans.xpath('./div[@class="info"]/div[1]/span[1]/text()').extract_first('')
            # 链接
            fans_href = fans.xpath('./div[@class="info"]/a/@href').extract_first('')
            fans_href = fans_href.split('/')[-1]
            fans_href = 'https://www.jianshu.com/users/' + fans_href + '/followers?page={}'
            count = int(fans.xpath('./div[@class="info"]/div[1]/span[2]/text()').re('粉丝 (.*)')[0])
            for i in range(1, count // 9 + 1):
                yield scrapy.Request(url=fans_href.format(i), callback=self.parse)
            yield item

