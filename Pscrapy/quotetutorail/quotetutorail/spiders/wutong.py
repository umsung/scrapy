# -*- coding: utf-8 -*-
import scrapy
import re

class WutongSpider(scrapy.Spider):
    name = 'wutong'
    allowed_domains = ['chinawutong.com']
    start_urls = ['http://www.chinawutong.com/201t1/beijing']
    headers = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',

    }

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url=url, callback=self.parse, headers=self.headers, dont_filter=True)

    # def parse(self, response):
    #     node_list = response.xpath('//div[@class="leftWapper"]/div/a')
    #     for node in node_list:
    #         url = node.xpath('./@href').extract_first()
    #         url = response.urljoin(url)
    #         yield scrapy.Request(url=url, callback=self.parse2)

    def parse(self, response):
        # next_page = response.xpath('//a[contains(./text(),"下一页")]/@href').extract_first()
        #
        # next_page = response.urljoin(next_page)
        # print(next_page)
        # yield scrapy.Request(url=next_page, callback=self.parse)

        node_list = response.xpath('//div[@class="bgWhite"]/ul/li')
        for node in node_list:
            item = {}
            url = node.xpath('./a/@href').extract_first()
            url = response.urljoin(url)
            print(url)
            yield scrapy.Request(url=url, callback=self.parse1, dont_filter=True, headers=self.headers)


    def parse1(self, response):
        next_page = response.xpath('//a[contains(./text(),"下一页")]/@href').extract_first()
        yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)

        node_list = response.xpath('//*[@class="tuiJian"]/div[1]/following-sibling::div')
        for node in node_list:
            # print(node.extract())
            item = {}
            a = ''.join(node.extract())
            # print(a)
            item['begin'] = re.search(r'<i>始：</i>.*?<a href=.*?>(.*?)</a>', a, re.S)
            if item['begin']:
                item['begin'] = re.sub('\s', '', item['begin'].group(1))

            item['end'] = re.search(r'<i>终：</i>.*?<a href=.*?>(.*?)</a>', a, re.S)
            if item['end']:
                item['end'] = re.sub('\s', '', item['end'].group(1))
            item['companyName'] = re.search(r'<a class=".*?companyName".*?>(.*?)</a>', a, re.S).group(1)
            item['leftAddress'] = re.search(r'<div class="leftAddress">(.*?)</div>', a, re.S).group(1)
            # item['begin'] = node.xpath('.//p[contains(./i[1]/text(),"始")]/a[1]/text').extract_first()
            # item['end'] = node.xpath('.//p[contains(./i[1]/text(),"终")]/a[1]/text').extract_first()
            # item['companyName'] = node.xpath('.//a[@class="fl companyName"]/text').extract_first()
            # item['leftAddress'] = node.xpath('.//div[@class="fl lineInfo1"]/div[last()]/text').extract_first()
            item['Heavy'] = node.xpath('.//li[contains(./i[1]/text(),"轻货")]/preceding-sibling::li[1]').xpath('string(.)').extract_first()
            if item['Heavy']:
                if '拼车' in item['Heavy']:
                    item['Heavy'] = re.sub('拼车：', '', item['Heavy']).strip()
            # else:
            #     item['Heavy'] = re.sub('重货：', '', item['Heavy']).strip()

            item['light'] = node.xpath('.//li[contains(./i[1]/text(),"轻货")]').xpath('string(.)').extract_first()
            # item['light'] = re.sub('轻货：', '', item['light']).strip()

            item['ageing'] = node.xpath('.//li[contains(./i[1]/text(),"时效")]').xpath('string(.)').extract_first()
            # item['ageing'] = re.sub('时效： ', '', item['ageing']).strip()

            item['rate'] = node.xpath('.//li[contains(./i[1]/text(),"频率")]').xpath('string(.)').extract_first()
            # item['rate'] = re.sub('频率：', '', item['rate']).strip()

            item['vote'] = node.xpath('.//li[contains(./text()[1],"最低一票")]').xpath('string(.)').extract_first()
            # item['vote'] = re.sub('最低一票：', '', item['vote']).strip()

            item['url'] = response.url
            yield item

