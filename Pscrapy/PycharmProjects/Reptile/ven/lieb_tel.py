import requests
from lxml import etree
import re

headers = {

'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}


# def index_parse1():
#     html = requests.get('http://zhengzhou.liebiao.com/shouji/502789516.html', headers=headers).text
#     resp = etree.HTML(html)
#     node_list = resp.xpath('//*[@class="subcate"]/a')
#     for node in node_list:
#         url = node.xpath('./@href')
#         return url
#
#
# def parse2(url):
#     html = requests.get(url, headers=headers).text
#     resp = etree.HTML(html)
#     node_list = resp.xpath('//*[@class="region"]/a[1]/following-sibling::a')
#     for node in node_list:
#         url = node.xpath('./@href')
#         return url


def parse3(url):
    html = requests.get(url, headers=headers).text
    resp = etree.HTML(html)
    node_list = resp.xpath('//*[@class="post clf"]')
    for node in node_list:
        url = node.xpath('./div[1]/div[2]/div[1]/h2/a/@href')[0]
        return url


def parse4(url):
    html = requests.get(url, headers=headers).text
    resp = etree.HTML(html)
    item = resp.xpath('//*[contains(./text(),"联系方式")]/@data-phone')
    # item['tel'] = response.xpath('//span[@class="phone"]/text()').extract_first()
    return item


def main():

    for i in range(1, 21):
        url = 'http://zhengzhou.liebiao.com/erqi/iphone/index' + str(i) + '.html'
        html = parse3(url)
        print(parse4(html))



if __name__ == '__main__':
    main()