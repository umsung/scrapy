# -*- coding: utf-8 -*-
import scrapy
import json

from scrapy import Request


class VideoSpider(scrapy.Spider):
    name = 'video'
    allowed_domains = ['gov.cn']
    start_urls = ['https://dyjy.dtdjzx.gov.cn/resourcelist?tdsourcetag=s_pctim_aiomsg']
    # f_list_url = 'https://dyjy.dtdjzx.gov.cn/resourcelist?classificationId={id}'
    # start_id = '2629387299537920'
    datas = []


    def start_requests(self):
        Payload = {
            'isSort': '1',
            'pageNo': '1',
            'pageSize': '15',

        }
        headers = {
            'Accept': 'ation/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '37',
            'Content-Type': 'application/json;charset=UTF-8',
            'Cookie': 'Hm_lvt_d652361e289e90df5f0bacaa8bf8cf2b=1544076964; X-SESSION=b93bea59-467b-4f74-bf2a-d3f1d3e63d1f; Hm_lpvt_d652361e289e90df5f0bacaa8bf8cf2b=1544085801',
            'Host': 'dyjy.dtdjzx.gov.cn',
            'Origin': 'https://dyjy.dtdjzx.gov.cn',
            'Referer': 'https://dyjy.dtdjzx.gov.cn/resourcelist',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
            # 'X-Requested-With': 'XMLHttpRequest',
        }
        # yield scrapy.FormRequest(url='https://dyjy.dtdjzx.gov.cn/course/special/findAll', callback=self.parse, formdata=json.dumps(Payload))
        postUrl = 'https://dyjy.dtdjzx.gov.cn/course/special/findAll'
        # yield Request(url=postUrl, headers=headers, meta={'payloadFlag': True, 'payloadData': Payload, 'headers': headers}, callback=self.parse)


        yield scrapy.Request(url=postUrl, method="POST", headers=headers, callback=self.parse, body=json.dumps(Payload))


    def parse(self, response):
        print(response.text)
    #     node_list = response.xpath  ('//*[@id="course-types-tree"]/li')
    #     for node in node_list:
    #         num_id = node.xpath('./a/@id').extract()[0]
    #         list_url = 'https://dyjy.dtdjzx.gov.cn/resourcelist?classificationId=' + num_id
    #         yield scrapy.Request(url=list_url, callback=self.list_parse)
    #
    # def list_parse(self, response):
    #     node_list = response.xpath('//*[@id="resource_list_html1"]/li')
    #     for node in node_list:
    #         title = node.xpath('./a/div[2]/text').extract()[0]
    #         detail_url = node.xpath('./a/@href').extract()[0]
    #         yield scrapy.Request(url=response.urljoin(detail_url), callback=self.detail_parse)
    #
    # def detail_parse(self, response):
    #     pass