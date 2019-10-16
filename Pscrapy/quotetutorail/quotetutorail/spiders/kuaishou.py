# -*- coding: utf-8 -*-
import requests
import scrapy
from lxml import etree
import re
from fontTools.ttLib import TTFont

class KuaishouSpider(scrapy.Spider):
    name = 'kuaishou'
    allowed_domains = ['kuaishou.com']
    start_urls = ['https://live.kuaishou.com/search/author?keyword=%E6%AF%8D%E5%A9%B4']

    def parse(self, response):
        # print(response.text)
        # node_list = response.xpath('//*[@class="author-card"]')
        # for node in node_list:
        #     # data = node.xpath('//p[@class="profile-card-user-info-counts"]/text()').extract()
        #     # # print(data)
        #     # adata = ''.join(node.extract())
        #     # item = {}
        #     #
        #     #
        #     #
        #     # bdata = re.search('<p class="profile-card-user-info-counts" data-v-74e18046>(.*?)</p>', adata, re.S)
        #     # item['bdata'] = bdata.group(1).strip().encode('unicode_escape')
        #     # a = item['bdata'][:-28].replace(b'\\u', b'\\')
        #     # a = a[:-28].replace(b'\\', b';').decode('utf-8').upper()
        #     # print(item['bdata'])
        #     # print(a)
        #     # # yield item


        next_url = response.xpath('//div[@class="search-action"]/a[2]/@href').extract_first()
        yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse)


        font_url = re.findall(r"url\('(https:.*\.ttf)'\)", response.text)[0]
        with open('on_kuaishou.ttf', 'wb') as f:
            f.write(requests.get(font_url).content)


        base_font = TTFont('base_kuaishou.ttf')
        base_font.saveXML('base_kuaishou.xml')
        base_uni = base_font.getGlyphOrder()

        dict_font = {'uniAACB': '4', 'uniABCD': '3', 'uniACDD': '0', 'uniAEFB': '8', 'uniAFBC': '6',
                     'uniBBCA': '1', 'uniBDCA': '5', 'uniBFEE': '9', 'uniCCAC': '2', 'uniCFBA': '7'}


        online_font = TTFont('on_kuaishou.ttf')
        on_dict= online_font.getBestCmap()


        selector = etree.HTML(response.body.decode('utf-8'))
        node_list = selector.xpath('//*[@class="author-card"]')
        for node in node_list:
            item = {}
            item['title'] = node.xpath('.//div[@class="profile-card-user-info-intro"]/@title')[0]

            i = etree.tostring(node).decode('utf-8')
            # print(i)
          #  data = re.search('<p class="profile-card-user-info-counts" data-v-74e18046="">(.*?)</p>', i, re.S)
            data = re.search('<p class="profile-card-user-info-counts" data-v-74e18046="">\s+(.*?)\s+(.*?)\s+(.*?)\s+</p>', i, re.S)

            # print(data.group())
            # print(data.group(1)[:-28])
            # print(data.group(2)[:-28])

            fans = data.group(1)[:-28].strip()
            fans = re.sub('&#', '', fans)
            follower = data.group(2)[:-28].strip()
            follower = re.sub('&#', '', follower)
            prod = data.group(3)[:-16].strip()
            prod = re.sub('&#', '', prod)
            print(fans)
            print(follower)
            print(prod)
            item['fans'] = []
            item['prod'] = []
            item['follower'] = []
            if fans != '':
                if '.' in fans:
                    fans = re.sub('\.', '.;', fans)
                    fans = fans.split(';')
                    for f in fans:
                        if f != '':
                            if f == '.' or f == 'w':
                                item['fans'].append(f)
                            else:
                                 item['fans'].append(jiemi(online_font, base_font, f, dict_font))
                else:
                    fans = fans.split(';')
                    for f in fans:
                        if f != '':
                            if f == '.' or f == 'w':
                                item['fans'].append(f)
                            else:
                                item['fans'].append(jiemi(online_font, base_font, f, dict_font))
                item['fans'] = ''.join(item['fans'])

            if follower != '':
                if '.' in follower:
                    follower = re.sub('\.', '.;', follower)
                    follower = follower.split(';')
                    for f in follower:
                        if f != '':
                            if f == '.' or f == 'w':
                                item['follower'].append(f)
                            else:
                                item['follower'].append(jiemi(online_font, base_font, f, dict_font))
                else:
                    follower = follower.split(';')
                    for f in follower:
                        if f != '':
                            if f == '.' or f == 'w':
                                item['follower'].append(f)
                            else:
                                item['follower'].append(jiemi(online_font, base_font, f, dict_font))
                item['follower'] = ''.join(item['follower'])

            if prod != '':
                if '.' in prod:
                    prod = re.sub('\.', '.;', prod)
                    prod = prod.split(';')
                    for f in prod:
                        if f != '':
                            if f == '.' or f == 'w':
                                item['prod'].append(f)
                            else:
                                item['prod'].append(jiemi(online_font, base_font, f, dict_font))
                else:
                    prod = prod.split(';')
                    for f in prod:
                        if f != '':
                            if f == '.' or f == 'w':
                                item['prod'].append(f)
                            else:
                                item['prod'].append(jiemi(online_font, base_font, f, dict_font))
                item['prod'] = ''.join(item['prod'])

            yield item


def jiemi(online_font, base_font, f, dict_font):
    on_uni = online_font.getBestCmap()[int(f)]
    on_obj = online_font['glyf'][on_uni]
    for bs_uni in base_font.getGlyphOrder():
        if base_font['glyf'][bs_uni] == on_obj:
            return dict_font[bs_uni]

# # 解析字体库
# temp = {}
# for i in range(10):
#     onlineGlyph = onlineFonts['glyf'][uni_list[i]]
#     for j in range(10):
#         baseGlyph = baseFonts['glyf'][base_fonts[j]]
#         if onlineGlyph == baseGlyph:
#             temp["&#x" + uni_list[i][3:].lower() + ';'] = base_nums[j]
#
# # 字符替换  把temp.kes 拼成(&#xABCD;|&#XSDFG|....)
# pat = '(' + '|'.join(temp.keys()) + ')'
#
# # 在根据pat 把对应的key.values替换
# response_index = re.sub(pat, lambda x: temp[x.group()],     response_index)
