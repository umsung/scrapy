# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
import re
import requests
from fontTools.ttLib import TTFont

class QichezhijiaSpider(scrapy.Spider):
    name = 'qichezhijia'
    allowed_domains = ['autohome.com.cn']
    start_urls = ['https://club.autohome.com.cn/bbs/thread/519b4c2f41839889/57421195-1.html']

    def parse(self, response):
        text = response.xpath('//div[@class="conttxt"]/div[1]').xpath('string(.)').extract()[0]
        print(text)
        font_url = 'https:' + re.search(r",url\('(.*\.ttf)'\)", response.text, re.S).group(1)
        # test = re.search(r' layer1="text-s"></div>新车已经行驶5500公里，现给<span.*?>(.*?)</span>', response.text, re.S)
        # text = response.xpath('//div[@class="conttxt"]/div[1]').xpath('string(.)').extract()
        # bb = "".join(text)
        # templetpate = re.search(r'<div class="w740">(.*?)<a href=".*?" name="shang"></a>', response.text, re.S).group(1)
        # cc = response.xpath('//div[@class="conttxt"]/div[1]//text()').extract()
        # cc = ''.join(cc)
        # print(bb)
        # print(cc)
        #
        # print(font_url)
        with open('online_qc.ttf', 'wb') as f:
            f.write(requests.get(font_url).content)

        base_font = TTFont('qiche.ttf')
        # base_font.saveXML('qiche.xml')
        base_uni = base_font.getGlyphOrder()[1:]
        print('base_uni', base_uni)

        online_font = TTFont('online_qc.ttf')
        # online_font.saveXML('online_qc.xml')
        online_uni = online_font.getGlyphNames()[1:]
        print('online_uni', online_uni)

        bm = online_font.getBestCmap()
        print('bm', bm)


        dict_font = {'uniEC1B': '八', 'uniEC6D': '大', 'uniEDAE': '右', 'uniECFA': '十', 'uniED4C': '呢', 'uniEC99': '四',
                     'uniECEB': '小', 'uniEC37': '好', 'uniED78': '三', 'uniEDCA': '是', 'uniED16': '短', 'uniEC63': '五',
                     'uniECB5': '下', 'uniEDF5': '少', 'uniEC53': '近', 'uniED94': '长', 'uniECE0': '地', 'uniED32': '多',
                     'uniEC7F': '更', 'uniEDBF': '左', 'uniEC1D': '不', 'uniED5E': '矮', 'uniEDAF': '和', 'uniECFC': '高',
                     'uniEC49': '一', 'uniEC9A': '很', 'uniEDDB': '的', 'uniED28': '六', 'uniED79': '得', 'uniECC6': '七',
                     'uniED18': '坏', 'uniEC64': '着', 'uniEDA5': '九', 'uniEDF7': '上', 'uniED43': '远', 'uniEC90': '低',
                     'uniECE2': '了', 'uniEC2E': '二'}

        temp = {}
        for bs_uni in base_uni:
            base_obj = base_font['glyf'][bs_uni]
            for ol_uni in online_uni:
                online_obj = online_font['glyf'][ol_uni]
                ol = ol_uni[3:]
                if base_obj == online_obj:
                    temp[eval(r"u'\u" + ol.lower() + "'")] = dict_font[bs_uni]

        # for i in range(38):
        #     base_obj = base_font['glyf'][base_uni[i]]
        #     for j in range(38):
        #         ol_obj = online_font['glyf'][online_uni[j]]
        #         if base_obj == ol_obj:
        #             # temp["&#x" + online_uni[j][3:].lower() + ';'] = dict_font[base_uni[i]]
        #             temp[eval(r"u'\u" + online_uni[j][3:].lower() + "'")] = dict_font[base_uni[i]]

        print(temp)

        # pat = '(' + '|'.join(temp.keys()) + ')'
        # text = re.sub(pat, lambda x: temp[x.group()], text)

        for i in range(38):
            text = text.replace(list(temp.keys())[i], list(temp.values())[i])

        print(text)

