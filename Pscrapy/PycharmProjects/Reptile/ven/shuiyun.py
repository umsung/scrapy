import csv

import requests
import re
import json
import pandas as pd
from json.decoder import JSONDecodeError

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}

def get_json_data(i):
    try:
        data = {
            'txtBackupType': '44000020190328003',
            'PageIndex': i,
            'PageSize': '10',
            # 'txtBackupContent': '',
            # 'backup_num': ''
        }
        resp = requests.post(url='http://121.33.200.100:8080/Pub/GetcredentialsBackup', data=data, headers=headers)

        print(resp.text)
        return resp.text
    except ConnectionError:
        print('ConnertionError')
        pass

def param_data(html):
    try:
        results = json.loads(html)
        itme = {}

        if 'rows' in results.keys():
            for row in results['rows']:
                id = row['id']
                irecord_apply_enter = row['record_apply_enter']
                backup_content = row['backup_content']
                address = re.findall('公司地址：(.*?)，', backup_content, re.S)
                phone = re.findall('联系电话：(.*?)，', backup_content, re.S)
                people = re.findall('法人代表：(.*)', backup_content, re.S)
                backup_time = row['backup_time']
                a.append([id,irecord_apply_enter,address,phone,people,backup_time])
    except JSONDecodeError:
        print("JSONDecodeError")
        pass

def save_data_csv():
    f = open('连接.csv', 'a', encoding='utf-8', newline='')
    a = csv.writer(f)
    return a

def save_data_pd(data):
    data = pd.DataFrame(data, columns=['id','名称','地址','电话','代表','时间'])
    data.to_csv('D:/l.csv', encoding='utf-8', index=0, mode='a+')

def save_data_json(data):
    f = open('json.csv', 'w', encoding='utf-8')
    line = json.dumps(data, ensure_ascii=False) + '\n'
    return f.write(line)

if __name__ == '__main__':
    a = []
    for i in range(1,168):
        print('正在爬取第{}页'.format(i))
        html = get_json_data(i)
        param_data(html)
    save_data_pd(a)