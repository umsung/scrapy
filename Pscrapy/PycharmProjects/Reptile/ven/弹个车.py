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

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'

  }
cookies = {'cookie': 'tt_webid=6618343718067275271; tt_webid=6618343718067275271; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=166c7f84b6e11a-09d3a6b3d82ccb-3b4a5a67-13c680-166c7f84b6f1bd; tt_webid=6618343718067275271; csrftoken=e770c6389ae385bbf7fba47f96c4158c; uuid="w:905d381d9b9e46c4aa84755a77637fce"; __tasessionId=bna4zyftr1540976040130; CNZZDATA1259612802=1030385221-1540951379-%7C1540972979'}


def get_page_index():
    data = {
        'agent': 7,
        'spm': '407.802989.5386188.1',
        'token': ''
    }
    resp = requests.get('https://fmc.souche-inc.com/activity/pcMarketApi/getSaleModelCar', headers=headers)
    try:
        if resp.status_code == 200:
            return resp.text
        return None
    except ConnectionError:
        return None


def parse_page_index(html):
    try:
        data = json.loads(html)
        print(data)
        a = []
        if data and 'data' in data.keys():
            for item in data.get('data'):
                if item:
                    yield [
                        item.get('seriesImg'),
                        item.get('tag'),
                        item.get('brandName'),
                        item.get('seriesName')
                    ]

                # car_name = item.get('brandName')
                # model = item.get('modelName')
                # tag = item.get('tag')
                # img = item.get('seriesImg')
                # a.append(car_name)
                # a.append(model)
                # a.append(tag)
                # a.append(img)
                # print(a)
    except JSONDecodeError:
        return None


def save_data_csv():
    f = open('弹个车.csv', 'a', encoding='utf-8', newline='')
    a = csv.writer(f)
    return a


def download_img(img_url, name):
    try:
        resp = requests.get(img_url, headers=headers, cookies=cookies)
        if resp.status_code == 200:
            save_img(resp.content, name)
        return None
    except ConnectionError:
        print("error occur")
        return None


def save_img(html_content, name):
    try:
        os.mkdir('tan_ge_che')
    except FileExistsError:
        pass
    img_name = md5(html_content).hexdigest()
#    print(img_name)
#    哈希函数md5().hexdigest()
    with open('./tan_ge_che/{}.jpg'.format(name), 'wb') as f:
        f.write(html_content)
        f.close()


def main():
    html = get_page_index()
    for img_href in parse_page_index(html):
        download_img(img_href[0], img_href[3])
        print(img_href[0])
        save_data_csv().writerow(img_href)


if __name__ == '__main__':
    main()