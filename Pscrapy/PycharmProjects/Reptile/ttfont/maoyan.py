# -*- coding: utf-8 -*-
import scrapy
import re
from fontTools.ttLib import TTFont
import requests
from lxml import etree

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/board/1']

    def parse(self, response):
        font_url = 'http:' + re.search(r"url\('(.*\.woff)'\)", response.text).group(1)
        with open('on_maoyan.woff', 'wb')as f:
            f.write(requests.get(font_url).content)

        base_font = TTFont('base_maoyan.woff')    # 获取基础字体对象
        # base_font.saveXML('base_maoyan.xml')
        base_uni = base_font.getGlyphOrder()[2:]  # 获取基础字体编码，从第二个开始
        print('base_uni:', base_uni)
        base_obj = base_font.getGlyphNames()[1:-1]  #获取基础字体字符对象

        print('base_obj:', base_obj)
        base_dict = {'uniE5A1': '9', 'uniF2B5': '5', 'uniE3BD': '8', 'uniF48F': '1', 'uniE6B8': '0',
                     'uniF03F': '2', 'uniEFB6': '6', 'uniF7EF': '7', 'uniF822': '3', 'uniF14B': '4'}



        online_font = TTFont('on_maoyan.woff')  # 获取动态字体对象
        online_font.saveXML('on_maoyan.xml')  # 将动态字体转成xml格式 查看结构

        on_name = online_font.getBestCmap()
        print('on_name:', on_name)


        online_uni = online_font.getGlyphOrder()[2:]
        print('online_uni:', online_uni)

        online_obj = online_font.getGlyphNames()[1:-1]
        print('online_obj:', online_obj)


        selector = etree.HTML(response.body.decode('utf-8'))
        node_list = selector.xpath('//*[@class="board-item-content"]')
        print(node_list)
        for node in node_list:
            print(node)
            item = {}
            item['title'] = node.xpath('.//p[@class="name"]/a/text()')[0]
            rt = node.xpath('.//p[@class="realtime"]/span/span/text()')[0]
            print('rt:', rt)
            print(etree.tostring(node))
            i = etree.tostring(node)
            a = node.xpath('.//p[@class="realtime"]/span/span/text()')
            print('a:', a)

            print(type(a[0]))
            print(type(i))

            print('a:', bytes(a[0], encoding = "utf8").decode('unicode-escape'))
            print('a:', a[0].encode('utf-8').decode('utf-8'))
            print('a[0]:', b'a'[0])
            print('a[0]:', b'a[0]'.decode('utf-8'))
            b = re.findall(b'span class="stonefont">(.*?)</span>', i)[0].decode('utf-8')
            print(b)
            b = re.sub('&#', '', b)
            b = re.sub('\.', '.;', b)
            b = b.split(';')
            item['p'] = []
            for i in b:
                if i != '':
                    if i == '.':
                        item['p'].append(i)
                    else:
                        item['p'].append(pojie(online_font, i, base_dict, base_uni, base_font))
            item['p'] = ''.join(item['p'])
            yield item
            # print('b:', b)
            # print('b[0]:', b[0])


            # item = {}
            # item['rt'] = node.xpath()


        # node_list = response.xpath('//*[@class="board-wrapper"]/dd')
        # #
        # # # node_list = etree.HTML(response.body.decode('utf-8')).xpath('//*[@class="board-wrapper"]/dd')
        # for node in node_list:
        #     item = {}
        #
        #     item['movie_name'] = node.xpath('.//p[@class="name"]/a/text()').extract_first()
        #     # item['r_pf'] = node.xpath('.//p[@class="realtime"]').xpath('string(.)').extract_first().strip()
        #     # item['r_pf'] = re.findall(b'<span class="stonefont">(.*?)</span>', etree.tostring(node))[0]
        #     # item['r_pf'] = re.sub('\s', '', item['r_pf']).encode('utf-8')
        #     # item['t_pf'] = node.xpath('.//p[@class="total-boxoffice"]').xpath('string(.)').extract_first().strip()
        #     item['t_pf'] = node.xpath('.//p[@class="realtime"]/span/span/text()').extract()[0]
        #     # item['t_pf'] = eval('b' + item['t_pf'])
        #     print(item['t_pf'])
        #
        #     item['t_f'] = node.xpath('.//p[@class="total-boxoffice"]/span/span/text()').extract()[0].strip()
        #     print(item['t_f'])
        #     # yield item


def pojie(online_font, p, base_dict, base_uni, base_font):
    on_uni = online_font.getBestCmap()[int(p)]
    on_obj = online_font['glyf'][on_uni]
    for bs_uni in base_uni:
        bs_obj = base_font['glyf'][bs_uni]
        if bs_obj == on_obj:
            return base_dict[bs_uni]







#
# # -*- coding: utf-8 -*-
# import scrapy
# from fontTools.ttLib import TTFont
# import re
# import requests
# from lxml import etree
#
#
# class MaoyanSpider(scrapy.Spider):
#     name = 'maoyan'
#
#     def start_requests(self):
#         self.start_urls = []
#         self.start_urls.append('http://maoyan.com/board/1')
#         for url in self.start_urls:
#             yield scrapy.Request(url=url, callback=self.parse)
#
#     def parse(self, response):
#         item = {}
#         # 获得字体url
#         style = ''.join(response.xpath('//style').extract())
#         font_url = 'http:' + ''.join(re.findall("url\('(.*?woff)'\)", style))
#         # 字体文件下载
#         font_response = requests.get(url=font_url)
#         with open('on_maoyan.woff', 'wb') as f:
#             f.write(font_response.content)
#         # 获得的字体转为xml格式
#         tfont = TTFont('on_maoyan.woff')
#         # 字体0101形状 tfont['glyf']['name']
#         tfont.saveXML('maoyan.xml')

#         # 参照的字体
#         basefont = TTFont('base_maoyan.woff')
#         # 作为[参照的] 所有数字的键
#         base_numlist = basefont.getGlyphNames()[1:-1]
#         # 作为参照的maoyanBase字体文件的映射关系
#         font_guanxi = {
#             'uniE877': '5', 'uniF0B5': '0', 'uniE3C8': '6', 'uniF076': '3', 'uniF833': '8',
#             'uniF079': '2', 'uniECED': '9', 'uniE49B': '1', 'uniEB89': '4', 'uniE56F': '7',
#         }
#         # 解密的字典
#
#         # 获取信息的节点
#         node = etree.HTML(response.body.decode('utf-8'))
#         node = node.xpath('//div[@class="board-item-content"]')
#         for i in node:
#             item['title'] = ''.join(i.xpath('.//p[@class="name"]/a/text()'))
#             piao = etree.tostring(i)
#             piao = re.findall(b'<span class="stonefont">(.*?)</span>', piao)[0]
#             # piao = re.sub(b'&#', b'', piao).decode('utf-8')
#             # piao = re.sub('\.', '.;', piao)
#             # piao = piao.split(';')
#             # item['piao'] = []
#             # for p in piao:
#             #     if p != '':
#             #         if p=='.':
#             #             item['piao'].append('.')
#             #         else:
#             #             item['piao'].append(jiemi(tfont, p, basefont, font_guanxi))
#             # item['piao']=''.join(item['piao'])
#             item['piao'] = piao
#             yield item


# def jiemi(tfont, code, basefont, guanxi):
#     """
#     :param tfont:现在字体文件
#     :param code: 字体的二进制编码
#     :param basefont: 作为参照的字体,TTFont实例
#     :param guanxi: 作为参照的字体的映射关系，字典
#     :return:
#     """
#     # 通过2进制code码拿到对应键名
#     tname = tfont.getBestCmap()[int(code)]
#     # 通过键名拿到字体形状
#     ph = tfont['glyf'][tname]
#     #
#     for basecode, basename in basefont.getBestCmap().items():
#         if basefont['glyf'][basename] == ph:
#             return guanxi[basename]









