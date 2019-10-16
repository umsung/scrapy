# -*- coding: utf-8 -*-
import scrapy
import re
from fontTools.ttLib import TTFont
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}

cookies = {
    'cookie': 'clientid=3; did=web_1bd7d44832132af359d0a43d9546ac2b; client_key=65890b29; kuaishou.live.bfb1s=3e261140b0cf7444a0ba411c6f227d88; didv=2'
}


def parse():

    resp = requests.get('https://live.kuaishou.com/search/author?keyword=%E6%AF%8D%E5%A9%B4&page=1', headers=headers, cookies=cookies)
    try:
        if resp.status_code == 200:
            return resp.text
        return resp.status_code
    except ConnectionError:
        return resp.status_code


def get_file(html):
    font_url = re.search(r"'(https:.*\.ttf)'", html).group(1)
    # 字体文件下载
    with open('快手.ttf', 'wb') as f:
        f.write(requests.get(font_url).content)
    font_name('快手.ttf')



def font_name(fone_file):
    # 手工构造映射关系
    number_map = {'period': '?', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': 6,
                  'sever': '7', 'eight': '8', 'nine': '9'}

    # 解析字体文件
    font = TTFont(fone_file)
    font.saveXML('kuaishou.xml')
    # 获取字体文件中的内容：zero到nine, 顺序随机
    font_content = font.getGlyphOrder()
    print(font_content)




    # 结果是['zero'......'nine']

    # num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    #
    # # 构造网页上对应的关系
    # error_dict_font = dict(zip(font_content, num))
    # right_dict_font = {}
    # for k, v in number_map.items():
    #     for x, y in error_dict_font.items():
    #         if k == x:
    #             right_dict_font[v] = y
    # print(right_dict_font)
    # return right_dict_font


def main():
    get_file(parse())


if __name__ == '__main__':
    main()