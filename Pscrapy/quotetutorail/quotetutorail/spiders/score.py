# -*- coding: utf-8 -*-
import json

import scrapy


class ScoreSpider(scrapy.Spider):
    name = 'score'
    allowed_domains = ['gsspaqw.org']
    # start_urls = ['http://www.gsspaqw.org/billyexjg/api/v1/score/scoreQListJson.do?page=1']
    url = 'http://www.gsspaqw.org/billyexjg/api/v1/score/scoreQListJson.do?page={page}'
    detail_url = 'http://www.gsspaqw.org/billyexjg/api/v1/score/scoreQListJson.do'

    def start_requests(self):
        for i in range(50, 100):

            yield scrapy.FormRequest(url=self.url.format(page=str(i)), callback=self.parse)

    def parse(self, response):
        results = json.loads(response.text)
        if results and 'rows' in results.keys():
            for rows in results['rows']:
                # print(rows)
                # item = {}

                ilegalno = rows['ilegalno']
                regno = rows['regno']
                id = rows['id']
                # print(ilegalno, regno)
                yield scrapy.FormRequest(url='http://www.gsspaqw.org/billyexjg/api/v1/score/getRecord.do', formdata={'ilegalno': str(ilegalno), 'regno': str(regno)}, callback=self.detail_parse)
    #
    def detail_parse(self, response):
        results = json.loads(response.text)
        if results and 'dispelList' in results.keys():
            for node in results['dispelList']:
                item = {}
                item['code'] = node['code']
                item['content'] = node['content']
                item['time'] = node['createtime']
                item['regper'] = node['regper']
                item['orgname']= node['orgname']
                item['deenforcename']= node['deenforcename']
                item['score']= node['score']
                item['ilegalno']= node['ilegalno']
                item['noticeId']= node['noticeId']

                yield item
        # print(results, response.url)


