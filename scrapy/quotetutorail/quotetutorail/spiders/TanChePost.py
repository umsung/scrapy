# -*- coding: utf-8 -*-
import json

import scrapy

from quotetutorail.items import TanChePostItem


class TanchepostSpider(scrapy.Spider):
    name = 'TanChePost'
    allowed_domains = ['tangeche.com', 'souche.com']
    start_urls = ['https://www.tangeche.com']
    index_url = 'https://leaseconsumer.souche.com//v1/secondCarSearchApi/querySecondCarListV2.json?agent=7&spm=407.802989.5386188.1&page={page}&pageSize=40'
    detail_url = 'https://leaseconsumer.souche.com//v1/followShopApi/getSecCarShopPage.json?agent=7&spm=32.783405.4879591.1&page=1&pageSize=1000&carType=1&carId={Id}'
    start_query = 1

    def start_requests(self):
        yield scrapy.Request(url=self.index_url.format(page=self.start_query), callback=self.parse)

    def parse(self, response):
        results = json.loads(response.body.decode('utf-8'))
        if 'data' in results.keys() and 'nextIndex' in results['data'].keys():
            for result in results['data']['items']:
                nextIndex = results['data']['nextIndex']
                item = TanChePostItem()
                for field in item.fields:
                    if field in result.keys():
                        item[field] = result[field]
                # yield item
                yield scrapy.Request(url=self.detail_url.format(Id=result['seriesId']), callback=self.detail_parse, meta={'item': item})
                yield scrapy.Request(url=self.index_url.format(page=nextIndex), callback=self.parse)

    def detail_parse(self, response):
        results = json.loads(response.text)
        item = response.meta['item']
        if 'data' in results.keys() and 'items' in results['data'].keys():
            for result in results['data']['items']:
                item['contactTel'] = result['contactTel']
                item['shopName'] = result['shopName']
                item['shopAddr'] = result['shopAddr']
                item['cityName'] = result['cityName']
                yield item



