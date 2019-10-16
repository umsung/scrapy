# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 19:37:38 2019

@author: iHJX_Alienware
"""

import requests
from bs4 import BeautifulSoup

u = 'https://comment.bilibili.com/115348295.xml'
r = requests.get(u)
# 显示采集的内容
r.encoding=r.apparent_encoding  # 万金油解决乱码问题
print(r.text)
    # 乱码问题
soup = BeautifulSoup(r.text, 'lxml')  # 解析网址 
dm_lst = soup.find_all('d')


#lst=[]
for i in dm_lst:
    dic = {}
    dic['其他信息'] = i['p']
    dic['弹幕内容'] = i.text
    print(dic)  # 将识别的内容，通过for循环，依次存入字典
    #lst.append(dic)  # 将字典dic添加进lst
    table.insert_one(dic)



import pandas as pd 
df = pd.DataFrame(lst)
df.to_excel('C:/Users/iHJX_Alienware/Desktop/r.xlsx')





