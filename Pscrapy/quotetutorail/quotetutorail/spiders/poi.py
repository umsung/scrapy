import scrapy
import re
from scrapy import Selector

# from poi.items import PoiItem


class PoispiderSpider(scrapy.Spider):
    name = 'poi'
    allowed_domains = ['poi58.com']
    start_urls = ['http://www.poi58.com/search/s/?homecity_name=%E5%8C%97%E4%BA%AC&cityid=80&wd=%E6%96%87%E5%8C%96%E5%85%AC%E5%8F%B8']


    def parse(self, response):
        selector = scrapy.Selector(response)
        nodeList = selector.xpath('.//*[@id="list"]/li')  # 初始网址
        count = 0
        for node in nodeList:
            count = count+1
        print(count)
        for i in range(count):
            items = {}
            # #联系电话
            items['number'] = selector.xpath('.//*[@id="list"]/li/div[2]/div/text()').extract()
            if len(items['number']) > i and items['number']:
                items['number'] = items['number'][i].strip()

            # #地址
            items['address'] = selector.xpath('.//*[@id="list"]/li/div[1]/div/text()').extract()
            if items['address']:
                items['address'] = items['address'][i].strip()

            # items['title'] = node.xpath('string(//ol[@id="list"]/li/h2/font)').extract()
            items['title'] = selector.xpath('.//ol[@id="list"]/li/h2/font').xpath('string(.)').extract()
            if items['title']:
                items['title'] = items['title'][i].strip()

            items['gps'] = selector.xpath('.//ol[@id="list"]/li/div[3]/div[1]/text()').extract()
            if items['gps']:
                items['gps'] = items['gps'][i].strip()

            items['tengxun'] = selector.xpath('.//ol[@id="list"]/li/div[3]/div[2]/text()').extract()
            if items['tengxun']:
                items['tengxun'] = items['tengxun'][i].strip()

            items['baidu'] = selector.xpath('.//ol[@id="list"]/li/div[3]/div[3]/text()').extract()
            if items['baidu']:
                items['baidu'] = items['baidu'][i].strip()

            yield items


        # next_url = response.xpath("//div/a[text()='下一页']/@href").extract_first()
        # if next_url:
        #     yield response.follow(next_url, callback=self.parse)
