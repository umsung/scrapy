# -*- coding: utf-8 -*-
import scrapy


class BaidushouluSpider(scrapy.Spider):
    name = 'baidushoulu'
    allowed_domains = ['baidu.com', 'baiducontent.com']
    start_urls = ['https://www.baidu.com/s?wd=site%3Awww.wine-world.com%20%E5%8D%9A%E5%BD%A9&pn=0&oq=site%3Awww.wine-world.com%20%E5%8D%9A%E5%BD%A9&ie=utf-8&rsv_idx=1&rsv_pq=82ebb37d0002aa51&rsv_t=5a3cG04ydE1GRvz6jFN3rd6r7gRMpxaf6KBXbUK7XCG3juwKLX%2BZ8z6%2FrxY']

    # def start_requests(self):
    #     for i in range(0, 34):
    #         print(i)
    #         yield scrapy.Request(url=self.urls.format(num=i*10), callback=self.parse)

    def parse(self, response):
        # keyword = response.xpath('//*[@id="kw"]/@value').extract_first()
        page = response.xpath('//*[@class="fk fk_cur"]/following-sibling::span[1]/text()').extract_first()
        print('正在爬取第{}页'.format(page))
        title = response.xpath('//*[@class="result c-container "]/h3/a/text()').extract()
        title_url = response.xpath('//*[@class="result c-container "]/h3/a/@href').extract()
        node_list = response.xpath('//*[@class="result c-container "]')
        # print(node_list)
        for node in node_list:
            # print(node)
            # item = {}
            # item['keyword'] = keyword
            # item['title'] = node.xpath('./h3/a/text()').extract_first()
            # item['title_url'] = node.xpath('./h3/a/@href').extract_first()
            # print(item['title'], item['title_url'])
            snapshot_url = node.xpath('//a[contains(./text(),"百度快照")]/@href').extract()
            # print(item['title'], item['title_url'], snapshot_url)
            for i in range(len(snapshot_url)):
                s_url = snapshot_url[i]
                # item['title'] = title[i]
                # item['title_url'] = title_url[i]
                # print(s_url)
                yield scrapy.Request(url=s_url, callback=self.detail_parse)
                # yield item
        next_page = response.xpath('//a[contains(./text(), "下一页")]/@href').extract_first()
        url = response.urljoin(next_page)
        yield scrapy.Request(url=url, callback=self.parse)

    def detail_parse(self, response):

        # print(response.url)
        item = {}
        # item = response.meta['item']
        item['snapshot_url'] = response.url
        href = response.xpath('//div[contains(./text()[1],"百度和网页")]/a/@href').extract_first()
        item['real_url'] = href
        yield item