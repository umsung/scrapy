# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
import re

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=残疾']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # print(response.text)
        # selector = etree.HTML(response.text)
        node_list = re.findall(r'<a rel="noreferrer" href="(.*?)".*?</a>', response.text, re.S)
        for node in node_list:
            if node.startswith('/p/'):
                url = 'https://tieba.baidu.com' + node
                yield scrapy.Request(url=url, callback=self.detail_parse)
        next_page = re.findall(r'.*?\n<a href="(.*?)" class="next pagination-item " >下一页&gt;</a>', response.text)[0]
        next_page = 'https' + next_page
        yield scrapy.Request(url=next_page,callback=self.parse)
        # for node in node_list:

        #     url = node.xpath('.//a[@class="j_th_tit "]/@href').extract()[0]
        #     print('url', url)
        #     # yield scrapy.Request(url=response.urljoin(url), callback=self.detail_parse)
        # next_page = response.xpath("//*[@id='frs_list_pager']").extract()
        # print('next_page', next_page)
        # yield scrapy.Request(url=next_page, callback=self.parse)

    def detail_parse(self, response):
        node_list = response.xpath("//*[@class='l_post l_post_bright j_l_post clearfix  ']")
        for node in node_list:
            item = {}
            title = response.xpath('//*[@id="j_core_title_wrap"]/h3/@title').extract()[0]
            author = node.xpath('.//li[@class="d_name"]/a/text()').extract()[0]
            author_face = node.xpath('.//li[@class = "icon"]/div/a/img/@src').extract()[0]
            content = node.xpath('.//div[@class="d_post_content j_d_post_content "]/text()').extract()[0].strip()
            time = node.xpath('.//div[@class="post-tail-wrap"]/span[last()]/text()').extract()[0]
            floor = node.xpath('.//div[@class="post-tail-wrap"]/span[last()-1]/text()').extract()[0]
            item['url'] = response.url
            item['title'] = title
            item['author'] = author
            item['author_face'] = author_face
            item['content'] = content
            item['time'] = time
            item['floor'] = floor
            img_list = node.xpath('.//img[@class="BDE_Image"]')
            print(img_list)
            if img_list:
                for img_url in img_list:
                    # print(img_url.xpath('./@src'))
                    img = img_url.xpath('./@src').extract()[0]
                    item['img'] = img
                    yield item
            else:
                item['img'] = ''
                yield item


