# -*- coding: utf-8 -*-
import csv
import json

from lxml import etree
import xlrd

# f = open('C:/Users/Administrator/Desktop/ex.xlsx', 'r', encoding= 'utf-8')
#
#
#
# print(f.read())

# excel_file = xlrd.open_workbook('C:/Users/Administrator/Desktop/test.xlsx')
#
# print(excel_file.sheet_names())
#
# sheet = excel_file.sheet_by_index(0)
#
# print(sheet.name, sheet.nrows, sheet.ncols)
#
# cols = sheet.col_values(1)
# rows = sheet.row_values(1)
# print(cols, rows)
#
# print(sheet.cell(1, 1).ctype)
#
# for col in cols:
#     print(col)


import pandas as pd
import requests
import re

df = pd.read_excel('D:/1.xlsx')
print(df['id'].tolist())

def get_data():
    id_list=df['id'].tolist()
    for id in id_list:
        url = 'http://121.33.200.100:8080/Pub/BeiAnPrint/?id={}'.format(id)
        resp = requests.get(url)
        # print(resp.text)
        selector = etree.HTML(resp.text)
        results = selector.xpath('//*[@class="print-body"]/div[1]')[0].xpath('string(.)')
        phone = re.findall('联系电话：(.*?)；', results, re.S)
        people = re.findall('法人代表：(.*)$', results, re.S)
        people = [people[0].strip() if len(people) else '无']
        print(id,phone,people)
        a.append([id,phone,people])

def save_data_csv():
    f = open('连接.csv', 'a', encoding='utf-8', newline='')
    a = csv.writer(f)
    return a

def save_data_pd(data):
    data = pd.DataFrame(data,columns = ['id','phone','people'])
    data.to_csv('people.csv', encoding='utf-8', index=0, mode='a+', header=False)

def save_data_json(data):
    f = open('json.csv', 'w', encoding='utf-8')
    line = json.dumps(data, ensure_ascii=False) + '\n'
    return f.write(line)


if __name__ == '__main__':
    a=[]
    get_data()
    save_data_pd(a)