import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import json
import os
import csv
from hashlib import md5
from multiprocessing import Pool
from json.decoder import JSONDecodeError
import time
from lxml import etree


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    # 'Referer': 'http://pay.hy.dglrqc.cn/index.php/cms/index/chapter/bid/28',
    'Content-Type': 'application/json; charset=utf-8',
    'Cookie': 'PHPSESSID=lf53u0lhsbarqm6vp2sf0es236',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
  }

def get_page_index():
    data = {
        "bid": "28",
        "start": 0,
        "limit": "100",
              }
    try:
        url = 'http://pay.hy.dglrqc.cn/index.php/cms/api/getchater/'
        resp = requests.get(url='http://pay.hy.dglrqc.cn/index.php/cms/api/getchater/', params=data, headers=headers)
        resp.encoding = 'utf-8'
        if resp.status_code == 200:
            print(resp.json())
            return resp.json()
    except JSONDecodeError:
        print("error occur")
        return None


def parse_page_index(html):
    try:
        data = json.loads(html)
        specialId = []
        if data and 'data' in data.keys():
            for item in data.get('data'):
                # specialId.append(item.get('specialId'))
                yield item.get('id')
        # print(specialId)
        # return specialId

    except JSONDecodeError:
        print("error occur")
        return None


def get_page_detail():
    try:
        resp = requests.post('http://pay.hy.dglrqc.cn/index.php/cms/index/detail/id/13032', headers=headers)
        resp.encoding = 'utf-8'
        jihe = []
        if resp.status_code == 200:
            # print(resp.text)
            html = resp.text.strip()
            html = html.replace('\\n', '')
            html = html.replace('\\', '')
            html = html.replace('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;', '')
            print(html)
            selector = etree.HTML(html)
            title = selector.xpath('/html/head/title')
            chapters = selector.xpath('//div[@class="read_tit_box"]')
            content = selector.xpath('//div[@class="read_main_p"]')[0].xpath('string(.)')
            # a = re.findall(r'<title>(.*?)<.*?>', html, re.S)
            jihe.append([title, chapters, content])
            print(content)

    except ConnectionError:
        print("error occur")
        return None


if __name__ == '__main__':
    get_page_detail()