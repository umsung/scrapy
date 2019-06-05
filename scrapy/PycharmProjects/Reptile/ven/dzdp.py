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
from multiprocessing import Pool


headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '234',
    'Content-Type': 'application/json',
    'Cookie': 's_ViewType=10; _lxsdk_cuid=167a12e4c4cc8-0c6bd3ec1714d7-546f3a7b-13c680-167a12e4c4dc8; _lxsdk=167a12e4c4cc8-0c6bd3ec1714d7-546f3a7b-13c680-167a12e4c4dc8; _hc.v=7c0c148c-3496-0230-0e2b-c80fa9b780ca.1544597425; cityid=7; logan_custom_report=; pvhistory=6L+U5ZuePjo8L2Vycm9yL2Vycm9yX3BhZ2U+OjwxNTQ0NTk4MjA3NTE2XV9b; m_flash2=1; default_ab=shop%3AA%3A1%7Cindex%3AA%3A1%7CshopList%3AA%3A1; msource=default; logan_session_token=slcx73holc8vw6jy95gj; _lxsdk_s=167a17f2e94-3f3-3d6-7b5%7C%7C1116',
    'Host': 'm.dianping.com',
    'Origin': 'http://m.dianping.com',
    'Referer': 'http://m.dianping.com/shenzhen/ch15',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    # 'X-Requested-With': 'XMLHttpRequest',
}

headers2 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 's_ViewType=10; _lxsdk_cuid=167a12e4c4cc8-0c6bd3ec1714d7-546f3a7b-13c680-167a12e4c4dc8; _lxsdk=167a12e4c4cc8-0c6bd3ec1714d7-546f3a7b-13c680-167a12e4c4dc8; _hc.v=7c0c148c-3496-0230-0e2b-c80fa9b780ca.1544597425; cityid=7; m_flash2=1; default_ab=shop%3AA%3A1%7Cindex%3AA%3A1%7CshopList%3AA%3A1; msource=default; logan_custom_report=; chwlsource=default; switchcityflashtoast=1; logan_session_token=vrfpm8u9ei59w1yizcb2; _lxsdk_s=167bffea304-84c-438-b1d%7C%7C197',
    'Host': 'm.dianping.com',
    'Referer': 'http://m.dianping.com/shenzhen/ch15/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'

}

def get_page_index(num):
    Payload = {
        'moduleInfoList': [{'moduleName': 'mapiSearch',
                            'query':
                                {'search':
                                    {
                                        'categoryId': '15',
                                        'cityId': '7',
                                        'keyword': '',
                                        'limit': '20',
                                        'locateCityid': '0',
                                        'maptype': '0',
                                        'parentCategoryId': '15',
                                        'regionId': '0',
                                        'sortId': '0',
                                        'start': str(num),
                                    }}
                            }],
        'pageEnName': 'shopList',
    }

    url = 'http://m.dianping.com/isoapi/module'
    resp = requests.post(url, data=json.dumps(Payload), headers=headers, allow_redirects=False)
    try:
        if resp.status_code == 200:
            return resp.text
        return None
    except ConnectionError:
        return None

def get_page_deatil(text):
    try:
        results = json.loads(text)
        print(results)

        if results and 'data' in results.keys():
            node_list = dict(results.get('data').get('moduleInfoList')[0]).get('moduleData').get('data').get(
                'listData').get('list')
            # print(node_list)
            if node_list:
                for node in node_list:
                    item = {}
                    item['name'] = node['name']
                    item['shopId'] = node['shopId']
                    item['priceText'] = node['priceText']
                    item['reviewCount'] = node['reviewCount']
                    item['matchText'] = node['matchText']
                    item['detail_url'] = 'http://m.dianping.com/shop/' + str(item['shopId'])
                    yield item
    except JSONDecodeError:
        return None

def detail_parse(url):
    resp = requests.get(url, headers=headers2)
    try:
        if resp.status_code == 200:
            # print(resp.text)
            return resp.text
        return None
    except ConnectionError:
        return None


def detail_parse2(html, url, n, s, p, r, m):
    # pass
    item = []
    a = re.search(r'<div class="aboutPhoneNum">.*?<a class="tel" href="(.*?)"', html, re.S)
    if a and a is not None:
        a = a.group(1)
    # # tel = re.sub('tel:', '', tel)
    b = re.search(r'<textarea style="display:none" id="shop-detail">.*?"address":"(.*?)"', html, re.S)
    if b and b is not None:
        b = b.group(1)

    item.append(a)
    item.append(b)
    item.append(url)
    item.append(n)
    item.append(s)
    item.append(p)
    item.append(r)
    item.append(m)

    print(item)


def main(num):
    text = get_page_index(num)
    if text:
        for item in get_page_deatil(text):
            if item['detail_url'] is not None:
                html = detail_parse(item['detail_url'])
                detail_parse2(html, item['detail_url'], item['name'], item['shopId'], item['priceText'], item['reviewCount'], item['matchText'])


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i*20 for i in range(1)])
