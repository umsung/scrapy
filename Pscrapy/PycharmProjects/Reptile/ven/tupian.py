# -*- coding: utf-8 -*-
import scrapy


class TupianSpider(scrapy.Spider):
    name = 'tupian'
    start_urls = ['http://pic.netbian.com/4kmeinv/index.html']

    # 爬虫开始时执行，有且仅执行一次
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 定位下一页
        try:
            next_url = response.xpath('//*[@id="main"]/div[4]/a[8]/@href').extract_first('')
            next_url = response.urljoin(next_url)
        except Exception:
            print('最后一页了！')
        else:
            yield scrapy.Request(url=next_url, callback=self.parse)
        # 定位初始
        pic_list = response.xpath('//*[@id="main"]/div[3]/ul/li/a')
        for pic in pic_list:
            # print(pic)
            # 定义空字典
            # item['pic_name'] = pic.xpath('./a/b/text()').extract_first('')
            pic_href = pic.xpath('./@href').extract_first('')
            pic_href = response.urljoin(pic_href)
            # item['pic_url'] = response.xpath('//*[@id="main"]/div[2]/div[1]/div[2]/a/img/@src').extract_first('')
            # item['pic_url'] = response.urljoin(item['pic_url'])
            yield scrapy.Request(url=pic_href, callback=self.parse_item)

    def parse_item(self, response):
        item = {}
        item['pic_name'] = response.xpath('//*[@id="main"]/div[2]/div[1]/div[1]/h1/text()').extract_first('')
        item['pic_url'] = response.xpath('//*[@id="img"]/img/@src').extract_first('')
        item['pic_url'] = response.urljoin(item['pic_url'])
        yield item
