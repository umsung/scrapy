# -*- coding: utf-8 -*-
import scrapy


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/apache?page=1']

    def parse(self, response):
        index_list = response.xpath('//*[@id="org-repositories"]/div[1]/div/ul/li/div[1]/h3/a')
        for index in index_list:
            url = index.xpath('./@href').extract_first()
            url = response.urljoin(url) + '/commits/'
            name = index.xpath('./text()').extract_first().strip()
            yield scrapy.Request(url=url, callback=self.detail_parse2, meta={"url": url, "name": name})
        next_url = response.xpath('//*[@id="org-repositories"]/div[1]/div/div/div/a[7]/@href').extract_first()
        next_url = response.urljoin(next_url)
        yield scrapy.Request(url=next_url, callback=self.parse)

    # def detail_parse1(self, response):
    #     time_list = response.xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[2]/div')
    #     for times in time_list:
    #         name = response.meta.get('name')
    #         # parse2_url = response.meta.get('url')
    #         parse2_url = response.xpath('//*[@id="js-repo-pjax-container"]/div[1]/div/h1/strong/a/@href').extract_first()
    #         parse2_url = response.urljoin(parse2_url) + '/commits'
    #         commit_time = times.xpath('./text()').extract()[1].strip()
    #         # print(parse2_url)
    #         # print(commit_time)
    #         yield scrapy.Request(url=parse2_url, callback=self.detail_parse2, meta={"name": name, "commit_time": commit_time, "parse2_url": parse2_url})

    def detail_parse2(self, response):
        table_list = response.xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[2]/ol')

        for tables in table_list:
            li_list = tables.xpath('./li')
            for table in li_list:
                item = {}
                item_name = response.meta.get('name')
                parse2_url = response.meta.get('url')
                commit_time = table.xpath('./div[1]/div/div[2]/relative-time/@datetime').extract_first()
                commit_name = table.xpath('./div[1]/div/div[2]/relative-time/preceding-sibling::*[1]/text() | ./div[1]/div/div[2]/relative-time/preceding-sibling::*[1]/text()').extract_first()
                btn_num = "'" + str(table.xpath('./div[2]/div/a/text()').extract_first().strip())
                url = table.xpath('./div[1]/p/a[1]/@href').extract_first()
                url = response.urljoin(url)
                item['item_name'] = item_name
                item['parse2_url'] = parse2_url
                item['commit_time'] = commit_time
                item['commit_name'] = commit_name
                item['btn_num'] = btn_num
                item['url'] = url

                yield scrapy.Request(url=response.urljoin(url), callback=self.detail_parse3, meta={"item": item})

    def detail_parse3(self, response):
        item = response.meta.get('item')
        changed_files = response.xpath('//*[@class="toc-diff-stats"]//*[contains(./text(),"file")]/text()').extract_first().strip().split()[0]
        additions = response.xpath('//*[@class="toc-diff-stats"]//*[contains(./text(),"addition")]/text()').extract_first().strip().split()[0]
        deletions = response.xpath('//*[@class="toc-diff-stats"]//*[contains(./text(),"deletion")]/text()').extract_first().strip().split()[0]
        item['changed_files'] = changed_files
        item['additions'] = additions
        item['deletions'] = deletions
        yield item


