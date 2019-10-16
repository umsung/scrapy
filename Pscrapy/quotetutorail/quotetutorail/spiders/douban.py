# -*- coding: utf-8 -*-
import scrapy
import re

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/subject/26752088/comments?start=0&limit=20&sort=new_score&status=P']

    urls = 'https://movie.douban.com/subject/26752088/comments?start={start}&limit=20&sort=new_score&status=P'

    def start_requests(self):
        for i in range(3):
            yield scrapy.Request(url=self.urls.format(start=i*20), callback=self.parse)

    def parse(self, response):
        item = {}
        movie_name = response.xpath('//*[@id="content"]/h1/text()').extract_first()
        Movie_name = re.sub('短评', '', movie_name)
        Release_time = response.xpath('//p[contains(./span/text(),"上映")]/text()').extract()
        Release_time = ''.join(Release_time).strip()

        item['Movie_name'] = Movie_name
        item['Release_time'] = Release_time
        yield item
