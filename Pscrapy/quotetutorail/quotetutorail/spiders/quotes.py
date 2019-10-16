# -*- coding: utf-8 -*-
import scrapy

from quotetutorail.items import QuotelItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # print(response.text)
        # print('状态吗:', response.status)
        quotes_list = response.css('div.quote')
        for quote in quotes_list:
            item = QuotelItem()
            title_xpath = quote.xpath('./span[1]/text').extract_first()
            title = quote.css('span.text::text').extract_first()
            author = quote.css('small.author::text').extract_first()
            tags = quote.css('div.tags > a.tag::text').extract()
            item['title'] = title
            item['author'] = author
            item['tags'] = tags
            yield item

        next_url = response.css('li.next > a::attr(href)').extract_first()
        if next_url:

            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse)



