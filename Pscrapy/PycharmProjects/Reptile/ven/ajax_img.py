# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:20:53 2018

@author: Administrator
"""
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


def get_page_index(keyword, offset):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1
              }
    params = urlencode(data)
    url = 'http://www.toutiao.com/search_content/' + '?' + params
    resp = requests.get(url, headers=headers, cookies=cookies)
    resp.encoding = 'utf-8'
    return resp.text


def parse_page_index(html):
    try:

        data = json.loads(html)
        if data and 'data' in data.keys():
            for item in data.get('data'):
                yield item.get('article_url')
    except JSONDecodeError:
        pass


def get_page_detail(detail_url):
    try:

        resp = requests.get(detail_url, headers=headers, cookies=cookies)
        resp.encoding = 'utf-8'
        if resp.status_code == 200:
            return resp.text
        return None
    except ConnectionError:
        print("error occur")
        return None


def parse_page_detail(detail_html, url):
    soup = BeautifulSoup(detail_html, 'lxml')
    title = soup.find('title').text
#    author = re.search(r'name: \'(.*?)\'', detail_html, re.S)
    # if title is not None and author is not None:
    #
    print(title)
    print(url)
    garlly = re.search(r'gallery: JSON.parse\("(.*?)"\)', detail_html, re.S)

    if garlly is not None:
        data = json.loads(garlly.group(1).replace('\\', ''))
        # print(garlly.group(1))
        # print(garlly.group(1).replace('\\', ''))
        # print(data)
        a = []
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [image.get('url') for image in sub_images]
            for image in images:
                download_img(image)
            # for items in data.get('sub_images'):
            #     img_url = items.get('url')
            #     print(img_url)
            #     download_img(img_url)
            a.append(title)
            a.append(url)
            a.append(images)
            save_data_csv().writerow(a)
            yield {
                'title': title,
                'url': url,
                'img_url': images
            }

# json.dumps(data)     将python字典类型的数据结构转成json格式的字符串
# json.loads(json_str) 将json格式的字符串转成python字典类型的数据结构
# json.dump 和 json.load则是对于文件，而不是字符串


def save_data(content):
    with open('头条数据.txt', 'a', encoding='utf-8', newline='') as f:

        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def save_data_csv():
    f = open('头条数据.csv', 'a', encoding='utf-8', newline='')
    a = csv.writer(f)
    return a


def download_img(img_url):
    try:
        resp = requests.get(img_url, headers=headers, cookies=cookies)
        if resp.status_code == 200:
            save_img(resp.content)
        return None
    except ConnectionError:
        print("error occur")
        return None


def save_img(html_content):
    try:
        os.mkdir('i_file')
    except FileExistsError:
        pass
#     img_name = md5(html_content).hexdigest()
# #    print(img_name)
# #    哈希函数md5().hexdigest()
#     with open('./im_file/{}.jpg'.format(img_name), 'wb') as f:
#         f.write(html_content)
#         f.close()
    filePath = './i_file/{}.jpg'.format(md5(html_content).hexdigest())
    # filePath = '{0}/{1}.{2}'.format(os.getcwd(), md5(html_content).hexdigest(), 'jpg')
    if not os.path.exists(filePath):
        with open(filePath, 'wb') as f:
            f.write(html_content)
            f.close()


def main(offset):
    html = get_page_index('图集', offset)

    for url in parse_page_index(html):
        if url is not None:

#            print(url)
#            print(get_page_detail(url))
            detail_html = get_page_detail(url)
#            print(detail_html)
            parse_page_detail(detail_html, url)
            for item in parse_page_detail(detail_html, url):
                save_data(item)




if __name__ == '__main__':

    # for i in range(4):
    #     main(i*20)
    pool = Pool()
    pool.map(main, [item*20 for item in range(2)])