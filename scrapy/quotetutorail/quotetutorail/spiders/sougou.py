# -*- coding: utf-8 -*-
import scrapy


class SougouSpider(scrapy.Spider):
    name = 'sougou'
    allowed_domains = ['sogou.com', 'sogoucdn.com']
    start_urls = ['https://www.sogou.com/web?query=site%3Awww.wine-world.com&from=index-nologin&sugsuv=1547629264271472&sut=6411&sugtime=1547629279729&lkt=24%2C1547629273319%2C1547629279524&s_from=index&sst0=1547629279729&page=1&ie=utf8&p=40040100&dp=1&w=01019900&dr=1']

    def parse(self, response):
        node_list = response.xpath('//a[contains(./text(),"快照")]')
        for node in node_list:
            href = node.xpath('./@href').extract_first()
            yield scrapy.Request(url=href, callback=self.detail_parse)
        next_page = response.xpath('//a[contains(./text(),"下一页")]/@href').extract_first()
        yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)

    def detail_parse(self, response):
        item = {}
        href = response.xpath('//p[contains(./text()[1],"搜狗与该网页")]/a/@href').extract_first()
        item['href'] = href
        yield item


