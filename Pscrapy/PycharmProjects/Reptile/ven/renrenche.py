# -*- coding: utf-8 -*-
import scrapy
import re
from fontTools.ttLib import TTFont
import requests

class RenrencheSpider(scrapy.Spider):
    name = 'renrenche'
    start_urls = ['https://www.renrenche.com/gz/ershouche/?&plog_id=bd49e5ed507aebb8599cdde8188a3eef']

    def start_requests(self):
        # for i in range(1, 5, 1):
        #     self.start_urls.append(
        #         'https://www.renrenche.com/gz/ershouche/p{}/?&plog_id=79d79d263044559732d687b64c258ab4'.format(i))
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        https://www.renrenche.com/gz/ershouche/p1/?&plog_id=79d79d263044559732d687b64c258ab4
        初步看了下，从列表页到内容页，并没有用ajax加载数据，只需要用xpath提取元素字段即可。
        打开源代码会发现，原来TM有“投毒”，源代码数据与显示数据不一致，看来这也是一种反爬措施
        """

        # html = response.body.decode('utf-8')
        # select = etree.HTML(html)
        # style = select.xpath('//style/text()')[0]
        # # url('https://misc.rrcimg.com/ttf/rrcttf86293b76594a1bf9ace9fd979b62db63.woff') format('woff')
        # font_url = re.search(r"url\('(.*?\.woff)'\) format\('woff'\),", str(style)).group(1)
        # 获取字体url
        font_url = re.findall('(https://misc.rrcimg.com.*\.ttf)', response.body.decode('utf-8'))[0]
        # 字体文件下载
        with open('人人车.ttf', 'wb') as f:
            f.write(requests.get(font_url).content)
        font_dict = font_name('人人车.ttf')

        node_list = response.xpath('//*[@id="search_list_wrapper"]/div/div/div[1]/ul//li')
        for node in node_list:
            item = {}
            # 车的名字
            item['car_name'] = node.xpath('./a/h3/text()').extract_first('')
            item['car_name'] = base_font(font_dict, item['car_name']), response.url
            # 车的信息
            item['car_info'] = node.xpath('./a/div[2]/span').xpath('string(.)').extract_first('')
            item['car_info'] = re.sub('\s', '', item['car_info'])
            item['car_info'] = base_font(font_dict, item['car_info']), response.url
            # 车的价格
            item['car_price'] = node.xpath('./a/div[4]/div/text()').extract_first('')
            item['car_price'] = re.sub('\s', '', item['car_price'])
            # 首付金额
            item['car_down_payment'] = node.xpath('./a/div[4]//div[@class="m-l"]/text()').extract_first('')
            # 链接
            item['car_link'] = node.xpath('./a/@href').extract_first('')
            item['car_link'] = response.urljoin(item['car_link'])

            yield scrapy.Request(url=item['car_link'], callback=self.parse_item, meta={'item': item})

        next_pages = response.xpath('//ul[@class="pagination js-pagination"]/li[last()]/a/@href').extract_first('')
        next_pages = response.urljoin(next_pages)
        yield scrapy.Request(url=next_pages, callback=self.parse)

    def parse_item(self, response):
        item = response.meta['item']
        # 新车购置税
        item['car_tax'] = response.xpath('//div[@class="middle-content"]/div/div').xpath('string(.)').extract_first('')
        item['car_tax'] = re.sub('\s', '', item['car_tax'])
        # 购买方式
        item['car_method'] = response.xpath('//div[@class="list payment-list"]/p[1]/text()').extract_first('')
        # 首付金额
        item['car_payment'] = response.xpath('//div[@class="list payment-list"]/p[2]/text()').extract_first('')
        # 月供金额
        item['car_month'] = response.xpath('//div[@class="list payment-list"]/p[3]/text()').extract_first('')
        # 服务费
        item['car_fee'] = response.xpath('//div[@class="detail-version3-service"]/p[2]').xpath(
            'string(.)').extract_first('')
        item['car_fee'] = re.sub('\s', '', item['car_fee'])
        # 车牌所在地
        item['car_location'] = response.xpath('//div[@class="licensed-city"]/p/strong/text()').extract_first('')
        # 外迁查询
        item['car_find'] = response.xpath('//li[@class="span5 car-fluid-standard"]/div/p/strong/text()').extract_first(
            '')
        # # 车辆到期时间
        # item['car_annual'] = response.xpath('//div[@class="info-about-car"]/div/ul/li[2]/text()').extract_first('')
        # item['car_annual'] = re.sub('\s', '', item['car_annual'])
        # # 商业险到期时间
        # item['car_insurance'] = response.xpath('//div[@class="info-about-car"]/div/ul/li[4]/text()').extract_first(
        #     default='')
        # item['car_insurance'] = re.sub('\s', '', item['car_insurance'])
        # # 有无发票
        # item['car_invoice'] = response.xpath('//div[@class="info-about-car"]/div/ul/li[6]/text()').extract_first(
        #     default='')
        # item['car_invoice'] = re.sub('\s', '', item['car_invoice'])
        # # 是否保养
        # item['car_maintenance'] = response.xpath('//div[@class="info-about-car"]/div/ul/li[8]/text()').extract_first(
        #     default='')
        # item['car_maintenance'] = re.sub('\s', '', item['car_maintenance'])

        yield item

def font_name(name):
    '''
    通过手敲的映射关系,解析字体文件
    '''
    number_map = {'eight': '8', 'five': '5', 'one': '1', 'nine': '9', 'period': '?', 'three': '3', 'six': '6',
                  'two': '2', 'seven': '7', 'four': '4', 'zero': '0'}
    # 下载下来的font文件
    font = TTFont(name)
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # 取出来font文件中的zero到nine,从第一个开始
    font_num = font.getGlyphOrder()[1:]
    # print('--------------',font_num)     # ['zero', 'one', 'two', 'three', 'four', 'five', 'seven', 'eight', 'six', 'nine']
    dic_font = dict(zip(num, font_num))
    # print('**************',dic_font)     # {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'seven', '7': 'eight', '8': 'six', '9': 'nine'}
    dict_num = {}
    for k, v in dic_font.items():
        for x, y in number_map.items():
            if dic_font[k] == x:
                dict_num[y] = k
    return dict_num

def base_font(dict, base_str):
    '''
    对照字典,解码字符串
    :param dict:
    :param base_str:
    :return:
    '''
    str_lis = []
    num_lis = list(dict.keys())
    for i in base_str:
        if i in num_lis:
            i = dict[i]
            str_lis.append(i)
        else:
            i = i
            str_lis.append(i)
    str_ = ''.join(str_lis)
    return str_
