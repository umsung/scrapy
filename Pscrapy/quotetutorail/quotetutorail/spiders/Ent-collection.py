# -*- coding: utf-8 -*-
# 企业信息爬虫
import scrapy
# from quotetutorail.quotetutorail.items import EntItem


class EntSpider(scrapy.Spider):
    name = 'Ent-collection'
    allowed_domains = ['poi58.com']
    base_url = 'http://www.poi58.com/search/s/?homecity_name={}&wd={}'
    custom_settings = {'ITEM_PIPELINES': {'quotetutorail.pipelines.EntPipline': 900}}

    def __init__(self , ct = None , kw = None , *args , **kwargs):
        print("sssssssssssssssssssss")
        print(ct)
        print(kw)
        super(EntSpider, self).__init__(*args, **kwargs)
        self.city = ct
        self.keyword = kw

    def start_requests(self):
        url = self.base_url.format(self.city, self.keyword)
        print("__________________________________________________________")
        print(str(url))
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        nodeList = response.xpath('//ol[@id="list"]') #初始网址
        for node in nodeList:
            item = EntItem()
            #名称
            item['name'] = node.xpath('./li/h2[@class="STYLE10"]/font').xpath('string(.)').extract()

            # 地址
            item['address'] = node.xpath('./li/div[@class="dig"]/div').xpath('string(.)').extract()

            #联系电话
            item['tel'] = node.xpath('./li/div[2][@class="dig"]/div').xpath('string(.)').extract()

            yield item

        next_url = response.xpath("//div/a[text()='下一页']/@href").extract_first() #爬取页数循环
        if next_url is not None:
            yield response.follow(next_url, callback=self.parse)

