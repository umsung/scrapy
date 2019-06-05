# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 16:20:44 2018

@author: Administrator
"""

import requests
from bs4 import BeautifulSoup
import time
import json
import datetime
import re
from fontTools.ttLib import TTFont
from lxml import etree
from multiprocessing import Process, Pool, Lock
import os
import threading

tlock = threading.Lock()
plock = Lock()

def param():
    print('thread %s is running...' % threading.current_thread().name)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'Cookie': '_ga=GA1.2.1884163979.1558064145; _gid=GA1.2.1721542062.1558666318; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1558064145,1558515373,1558666318; XSRF-TOKEN=eyJpdiI6IkZ6K0g3TFwvUFI1NVR2WXRUdHpteU5nPT0iLCJ2YWx1ZSI6IlZrM3hoSHVJd1VIU2dIZXNlTlVPblQ0ZFBRcjdxT2lVNXRLVm1ZS2pIVXZQK1JLcXFJK1NScWJGTVllV3pheHEiLCJtYWMiOiI0NTQ3MDliYmZlMDlmOTU0ZTdjNzEyN2ZjY2E1NGQxMWZjNTM4ZTc5OWExODcwNGM4MDg2OWE5YWEwOWI3MWYzIn0%3D; glidedsky_session=eyJpdiI6Ijk0cDhrazk4bTRhdGV3RUxXRTU3Z3c9PSIsInZhbHVlIjoiV0xHUzRock00YUI5QzNFcVU0Y0ducG1tOTY1dnZrckh2SFAyVllEQ1hMWFR5SUxLTVVhemZ0bDd5NGlWbWx6VSIsIm1hYyI6IjgyOGIxYTkzYTEzMDJkYmE2OWY5ZThlOGFhMjM5NWYxNGM4ZWU5ODA0ZDU2YTdhOGUwY2I5MGEzYzBjZDA3NDgifQ%3D%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1558667397'
    }
    s = 0
    for i in range(1, 5):
        # tlock.acquire()
        plock.acquire()
        try:
            resp = requests.get(url='http://glidedsky.com/level/web/crawler-font-puzzle-1?page={}'.format(i), headers=headers).text

            woff_url = re.search(r'src: url\("(.*?.woff)"\)', resp).group(1)
            print(woff_url)

            with open('font.woff', 'wb') as f:
                f.write(requests.get(woff_url).content)

            selector = etree.HTML(resp)
            nodes = selector.xpath('//*[@class="col-md-1"]')
            item = {}
            for node in nodes:
                item['num'] = pojie(dict_map('font.woff'), node.xpath('./text()')[0])
                print(item['num'])
                s = s+int(item['num'])
            print('sum:', s)
        finally:
            # tlock.release()
            plock.release()


def dict_map(woff_font):
    '''
    通过手敲的映射关系,解析字体文件
    '''
    number_map = {'cid00025': '8', 'cid00022': '5', 'cid00018': '1', 'cid00026': '9', 'period': '?', 'cid00020': '3', 'cid00023': '6',
                  'cid00019': '2', 'cid00024': '7', 'cid00021': '4', 'cid00017': '0'}
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    fonts = TTFont(woff_font)

    fonts.saveXML('111.xml')
    uni = fonts.getBestCmap().values()
    # print(uni)
    error_dict_font = dict(zip(uni, num))
    # print(error_dict_font)

    item = {}
    for x, y in error_dict_font.items():
        for k, v in number_map.items():
            if x == k:
                item[y] = v
    # print(item)
    return item


def pojie(dict, str):
    str_list = []
    keys = dict.keys()
    for i in str:
        if i in keys:
            str_list.append(dict[i])
    return ''.join(str_list)


if __name__ == '__main__':

    print('Parent process %s.' % os.getpid())
    # p = Process(target=param)
    p = Pool(4)   #同时放入4个进程
    for i in range(4):
        p.apply_async(param)
    print('Child process will start.')
    # p.start()
    p.close()
    p.join()
    print('Child process end.')

    # t = threading.Thread(target=param)
    # t1 = threading.Thread(target=param)
    # print('threading %s running' % threading.current_thread().name)
    # t.start()
    # t1.start()
    # t.join()
    # t1.join()
    # print('threading %s ended' % threading.current_thread().name)
