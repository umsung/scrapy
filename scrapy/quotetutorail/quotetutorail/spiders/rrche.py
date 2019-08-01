# -*- coding: utf-8 -*-
import scrapy
import re
from fontTools.ttLib import TTFont
import requests

class RenrencheSpider(scrapy.Spider):
    name = 'rrche'
    start_urls = ['https://www.renrenche.com/gz/ershouche/?&plog_id=bd49e5ed507aebb8599cdde8188a3eef']

    def parse(self, response):
        """
        https://www.renrenche.com/gz/ershouche/p1/?&plog_id=79d79d263044559732d687b64c258ab4
        初步看了下，从列表页到内容页，并没有用ajax加载数据，只需要用xpath提取元素字段即可。
        打开源代码会发现，原来TM有“投毒”，源代码数据与显示数据不一致，看来这也是一种反爬措施
        """
        tff_ = re.search(r"url\('(https:.*\.ttf)'\)", response.text).group(1)
        print(tff_)
        with open('templetpate.tff', 'wb') as f:
            f.write(requests.get(tff_).content)
        font_dict = font_name('templetpate.tff')

        node_list = response.xpath('//*[@id="search_list_wrapper"]/div/div/div[1]/ul/li[contains(./div/text(),"免费咨询")]')
        for li in node_list:
            item = {}

            item['car_name'] = li.xpath('./a/h3/text()').extract_first()
            item['car_name'] = base_font(font_dict, item['car_name'])

            item['index_url'] = response.url

            item['car_info'] = li.xpath('./a/div[2]/span').xpath('string(.)').extract_first().strip()
            item['car_info'] = base_font(font_dict, item['car_info'])

            item['price'] = li.xpath('./a/div[4]/div[1]/text()[1]').extract_first().strip()

            item['f_pay'] = li.xpath('./a//div[@class="down-payment"]/div/text()').extract_first()

            item['car_link'] = response.urljoin(li.xpath('./a/@href').extract_first())

            yield scrapy.Request(url=item['car_link'], callback=self.parse_item, meta={'item': item})

        next_url = response.xpath('//*[@class="pagination js-pagination"]/li[last()]/a/@href').extract_first()
        yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse)


    def parse_item(self, response):
        item = response.meta['item']
        item['car_method'] = response.xpath('//*[@id="zhimaicar-detail-header-right"]/div[3]/div[6]/p[1]/text()').extract_first()

        item['m_pay'] = response.xpath('//*[@id="zhimaicar-detail-header-right"]/div[3]/div[6]/p[3]/text()').extract_first()

        item['kilometre'] = response.xpath('//*[contains(./p[2]/text(),"行驶里程")]/p[1]/strong/text()').extract_first()

        item['car-licensed'] = response.xpath('//*[contains(./p[2]/text(),"车牌所在地")]/p[1]/strong/text()').extract_first()

        item['car-summary'] = response.xpath('//*[contains(./p[2]/text(),"变速箱")]/p[1]/strong/text()').extract_first()

        item['car-transfer'] = response.xpath('//*[contains(./p[2]/text(),"过户记录")]/p[1]/strong/text()').extract_first()

        yield item


def font_name(fone_file):
    # 手工构造映射关系
    number_map = {'period': '?', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': 6,
                  'seven': '7', 'eight': '8', 'nine': '9'}

    # 解析字体文件
    font = TTFont(fone_file)

    # 获取字体文件中的内容：zero到nine, 顺序随机
    font_content = font.getGlyphOrder()[1:]   # 获取所有编码
    # 结果是['zero'......'nine']

    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # 构造网页上对应的关系
    error_dict_font = dict(zip(font_content, num))
    right_dict_font = {}
    for k, v in number_map.items():
        for x, y in error_dict_font.items():
            if k == x:
                right_dict_font[v] = y
    return right_dict_font


def base_font(base_dict, base_str):
    a = []
    d_list = list(base_dict.keys())
    for i in base_str:
        if i in d_list:
            i = base_dict[i]
            a.append(i)
        else:
            i = i
            a.append(i)
    return ''.join(a)





# def font_name(name):
#     '''
#     通过手敲的映射关系,解析字体文件
#     '''
#     number_map = {'eight': '8', 'five': '5', 'one': '1', 'nine': '9', 'period': '?', 'three': '3', 'six': '6',
#                   'two': '2', 'seven': '7', 'four': '4', 'zero': '0'}
#     # 下载下来的font文件
#     font = TTFont(name)
#     num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     # 取出来font文件中的zero到nine,从第一个开始
#     font_num = font.getGlyphOrder()[1:]
#     # print('--------------',font_num)     # ['zero', 'one', 'two', 'three', 'four', 'five', 'seven', 'eight', 'six', 'nine']
#     dic_font = dict(zip(num, font_num))
#     # print('**************',dic_font)     # {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'seven', '7': 'eight', '8': 'six', '9': 'nine'}
#     dict_num = {}
#     for k, v in dic_font.items():
#         for x, y in number_map.items():
#             if dic_font[k] == x:
#                 dict_num[y] = k
#     return dict_num
#     # ------------------  # {'0':'0','1':'1','2':'2'........'9':'9'}
#
# def base_font(dict, base_str):
#     '''
#     对照字典,解码字符串
#     :param dict:
#     :param base_str:
#     :return:
#     '''
#     str_lis = []
#     num_lis = list(dict.keys())
#     for i in base_str:
#         if i in num_lis:
#             i = dict[i]
#             str_lis.append(i)
#         else:
#             i = i
#             str_lis.append(i)
#     str_ = ''.join(str_lis)
#     return str_
