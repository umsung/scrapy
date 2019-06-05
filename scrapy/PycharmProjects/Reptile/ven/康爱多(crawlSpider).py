# -*- coding: utf-8 -*-

import re
import json
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class KadSpider(CrawlSpider):
    name = 'kad'
    start_urls = ['http://www.360kad.com/dymhh/allclass.shtml']

    rules = (
        # http://search.360kad.com/?pageText=%E8%83%86%E5%9B%8A%E7%82%8E
        # http://search.360kad.com/?pageText=%E5%9D%90%E9%AA%A8%E7%A5%9E%E7%BB%8F%E7%97%9B
        # http://www.360kad.com/Category_783/Index.aspx
        # http://www.360kad.com/Category_1133/Index.aspx
        # 进入列表页
        Rule(LinkExtractor(allow=r'search.360kad.com', restrict_xpaths='//*[@id="ksBoxs"]'), follow=True),
        # 进入同级列表页
        Rule(LinkExtractor(allow=(r'/Category_(\d+)/Index.aspx', r'Pagetext=(.*?)&pageIndex=')), follow=True),

        # 进入详情页
        # /product/1010597010.shtml
        # /product/80355.shtml
        # http://www.360kad.com/product/130201.shtml?kzone=kadsearch&pagetext=支气管炎
        # http://www.360kad.com/product/130201.shtml
        # 限制xpath
        # /html/body/div[4]/div[2]/div[2]/ul
        # 或 //ul[@class="Productlist"]
        # //*[@id="YproductList"]
        Rule(LinkExtractor(allow=r'/product/(\d+).shtml'), callback='parse_item', follow=True,
             process_links='process_urls'),
    )

    def process_urls(self, links):
        # print(links)
        for link in links:
            link.url = link.url.split('?')[0]
        return links

    def parse_item(self, response):
        item = {}
        item['check_url'] = response.url
        item['drug_name'] = response.xpath('//h1/text()').extract_first('')
        # http://www.360kad.com/product/130201.shtml
        item['drug_id'] = re.findall('/(\d+)\.', response.url)[0]
        item['price_url'] = 'http://www.360kad.com/product/getprice?wareskucode={}'.format(item['drug_id'])

        yield scrapy.Request(url=item['price_url'], callback=self.parse_price, meta={'item':item})

    def parse_price(self, response):
        item = response.meta['item']
        d = json.loads(response.body.decode('utf-8'))
        item['drug_price'] = d['StyleInfo']['Price']
        yield item

