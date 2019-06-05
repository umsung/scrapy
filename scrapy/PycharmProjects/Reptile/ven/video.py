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
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '84',
        'Content-Type': 'application/json',
        'Cookie': 'Hm_lvt_d652361e289e90df5f0bacaa8bf8cf2b=1543976369; X-SESSION=fdfb66b6-ed73-43fc-bb54-87b1041dd1e7; Hm_lpvt_d652361e289e90df5f0bacaa8bf8cf2b=1543994136',
        'Host': 'dyjy.dtdjzx.gov.cn',
        'Origin': 'https://dyjy.dtdjzx.gov.cn',
        'Referer': 'https://dyjy.dtdjzx.gov.cn/resourcelist',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
  }


headers2 = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '26',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'Hm_lvt_d652361e289e90df5f0bacaa8bf8cf2b=1543976369; X-SESSION=b9430e90-c286-43fb-9cac-5a88fd124f9c; Hm_lpvt_d652361e289e90df5f0bacaa8bf8cf2b=1543998918',
        'Host': 'dyjy.dtdjzx.gov.cn',
        'Origin': 'https://dyjy.dtdjzx.gov.cn',
        'Referer': 'https://dyjy.dtdjzx.gov.cn/course/special/subject/2982776468030464',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',

    }

def get_page_index(num):
    Payload = {
        'isSort': '1',
        'pageNo': str(num),
        'pageSize': '15',
    }
    url = 'https://dyjy.dtdjzx.gov.cn/course/special/findAll'
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
        if results and 'data' in results.keys():
            for data in results.get('data'):
                if data:
                    yield {
                            'specialId': data.get('specialId')
                    }
    except JSONDecodeError:
        return None



def get_detail(url, data):

    param = {
        'specialId': str(data)
    }
    try:
        resp = requests.post(url=url, data=param, headers=headers2, allow_redirects=False)
        results = json.loads(resp.text)
        if results and 'course' in results.keys():
            for course in results.get('course'):
                if course:
                    courseId = course.get('courseId')
                    # print(courseId, data)
                    video_url = 'https://dyjy.dtdjzx.gov.cn/resourcedetailed/' + str(courseId) + '/' + str(data)
                    title = course.get('courseName')
                    current_url = 'https://dyjy.dtdjzx.gov.cn/course/special/subject/' + str(data)
                    a = []
                    a.append(title)
                    a.append(video_url)
                    a.append(current_url)
                    print(video_url, title)
                    save_data_csv().writerow(a)

    except JSONDecodeError:
        return None


def save_data_csv():
    f = open('video.csv', 'a', encoding='utf-8', newline='')
    a = csv.writer(f)
    return a


def main():
    for i in range(1, 22):
        text = get_page_index(i)
        for p_id in get_page_deatil(text):
            print(p_id['specialId'])

            url = 'https://dyjy.dtdjzx.gov.cn/course/special/queryBySpecialId'
            get_detail(url, p_id['specialId'])


if __name__ == '__main__':
    main()