# -*- coding: utf-8 -*-
import scrapy
import json
import re


class TgcSpider(scrapy.Spider):
    name = 'tgc'
    datas = []

    # 爬虫开始时执行，有且仅执行一次
    def start_requests(self):
        for i in range(1, 931):
            self.datas.append({
                'agent': '7',
                'spm': '407.802989.5386188.1',
                'page': str(i),
                'pageSize': '40',
            })
        for data in self.datas:
            yield scrapy.FormRequest(
                url='https://leaseconsumer.souche.com//v1/secondCarSearchApi/querySecondCarListV2.json', 
                callback=self.parse, formdata=data)

    def parse(self, response):
        d = json.loads(response.body.decode('utf-8'))
        d = d['data']['items']
        for i in d:
            item = {}
            item['seriesName'] = i['seriesName']
            item['modelName'] = i['modelName']
            item['modelName'] = re.sub('\s', '', item['modelName'])
            carId = i['id']
            item['mileageStr'] = i['mileageStr']
            item['prepaidAmountStr'] = i['prepaidAmountStr']
            item['cityName'] = i['cityName']
            item['installmentStr'] = i['installmentStr']
            yield scrapy.FormRequest(url='https://leaseconsumer.souche.com//v1/followShopApi/getSecCarShopPage.json',
                                     callback=self.parse_item,
                                     formdata={'agent': '7', 
                                               'spm': '407.802989.5386188.1', 
                                               'page': '1',
                                               'pageSize': '1000',
                                               'carType': '1', 
                                               'carId': carId, }, 
                                               meta={'item': item})

    def parse_item(self, response):
        item = response.meta['item']
        d = json.loads(response.body.decode('utf-8'))
        d = d['data']['items']
        for i in d:
            item['shopName'] = i['shopName']
            item['shopAddr'] = i['shopAddr']
            item['tel'] = i['contactTel']
            yield item
