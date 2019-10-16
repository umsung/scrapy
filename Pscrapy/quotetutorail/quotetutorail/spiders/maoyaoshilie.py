# -*- coding: utf-8 -*-
import scrapy
from fontTools.ttLib import TTFont
import re
import requests
from lxml import etree


class MaoyanshilieSpider(scrapy.Spider):
    name = 'maoyanshilie'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/board/1']

    def start_requests(self):
        self.start_urls = []
        self.start_urls.append('http://maoyan.com/board/1')
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = {}
        # 获得字体url
        style = ''.join(response.xpath('//style').extract())
        font_url = 'http:' + ''.join(re.findall("url\('(.*?woff)'\)", style))
        # 字体文件下载
        font_response = requests.get(url=font_url)
        with open('on_maoyan.woff', 'wb') as f:
            f.write(font_response.content)
        # 获得的字体转为xml格式
        tfont = TTFont('base_maoyan.woff')
        # 字体0101形状 tfont['glyf']['name']
        tfont.saveXML('shilie_maoyan.xml')
        # 参照的字体
        basefont = TTFont('on_maoyan.woff')
        # 作为[参照的] 所有数字的键
        base_numlist = basefont.getGlyphNames()[1:-1]
        # 作为参照的maoyanBase字体文件的映射关系
        font_guanxi = {
            'uniE877': '5', 'uniF0B5': '0', 'uniE3C8': '6', 'uniF076': '3', 'uniF833': '8',
            'uniF079': '2', 'uniECED': '9', 'uniE49B': '1', 'uniEB89': '4', 'uniE56F': '7',
        }
        # 解密的字典

        # 获取信息的节点
        node = etree.HTML(response.text)
        node = node.xpath('//div[@class="board-item-content"]')
        for i in node:
            item['title'] = ''.join(i.xpath('.//p[@class="name"]/a/text()'))
            piao = etree.tostring(i)
            piao = re.findall(b'<span class="stonefont">(.*?)</span>', piao)[0]
            print(piao)
            piao = re.sub(b'&#', b'', piao).decode('utf-8')
            piao = re.sub('\.', '.;', piao)
            piao = piao.split(';')
            print(piao)
            item['piao'] = piao
            item['piao'] = []
            for p in piao:
                if p != '':
                    if p=='.':
                        item['piao'].append('.')
                    else:
                        item['piao'].append(jiemi(tfont, p, basefont, font_guanxi))
            item['piao']=''.join(item['piao'])
            yield item
#
#
def jiemi(tfont, code, basefont, guanxi):
    """
    :param tfont:现在字体文件
    :param code: 字体的二进制编码
    :param basefont: 作为参照的字体,TTFont实例
    :param guanxi: 作为参照的字体的映射关系，字典
    :return:
    """
    # 通过2进制code码拿到对应键名
    tname = tfont.getBestCmap()[int(code)]
    # 通过键名拿到字体形状
    ph = tfont['glyf'][tname]
    #
    for basecode, basename in basefont.getBestCmap().items():
        if basefont['glyf'][basename] == ph:
            return guanxi[basename]
