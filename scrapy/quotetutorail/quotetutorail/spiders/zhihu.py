# -*- coding: utf-8 -*-
import json
from json import JSONDecodeError

import scrapy

from quotetutorail.items import ZhiHuItem


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    start_user = "excited-vczh"
    #储存查询URL和查询参数
    #个人信息
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_query = 'allow_message%2Cis_followed%2Cis_following%2Cis_org%2Cis_blocking%2Cemployments%2Canswer_count%2Cfollower_count%2Carticles_count%2Cgender%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'

    #关注列表
    follow_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    follow_query = 'data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'

    #被关注列表
    follower_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'
    follower_query = 'data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'

    def start_requests(self):
        yield scrapy.Request(url=self.user_url.format(user=self.start_user, include=self.user_query), callback=self.parse)
        yield scrapy.Request(url=self.follow_url.format(user=self.start_user, include=self.follow_query, offset=0, limit=20), callback=self.follow_parse)
        yield scrapy.Request(url=self.follower_url.format(user=self.start_user, include=self.follower_query, offset=0, limit=20), callback=self.follower_parse)

    def parse(self, response):
        try:
            results = json.loads(response.text)
            item = ZhiHuItem()
            for field in item.fields:
                if field in results.keys():
                    item[field] = results.get(field)
        except JSONDecodeError:
            pass
        yield item
        yield scrapy.Request(url=self.follow_url.format(user=results['url_token'], include=self.follow_query, offset=0, limit=20), callback=self.follow_parse)
        yield scrapy.Request(url=self.follower_url.format(user=results['url_token'], include=self.follower_query, offset=0, limit=20), callback=self.follower_parse)

    def follow_parse(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                url_token = result.get('url_token')
                yield scrapy.Request(url=self.user_url.format(user=url_token, include=self.follow_query), callback=self.parse)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == 'false':
            next_page = results.get('paging').get('next')
            yield scrapy.Request(url=next_page, callback=self.follow_parse)

    def follower_parse(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                url_token = result.get('url_token')
                yield scrapy.Request(url=self.user_url.format(user=url_token, include=self.user_query), callback=self.parse)

        if 'paging' in results.keys() and results['paging']['is_end'] == 'false':
            next_page = results.get('paging').get('next')
            yield scrapy.Request(url=next_page, callback=self.follower_parse)


