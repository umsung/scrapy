# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 17:06:08 2018

@author: Administrator
"""
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
#设置列表页URL的固定部分
url='http://bj.lianjia.com/ershoufang/'
#设置页面页的可变部分
page=('pg')
for i in range(1,5):
     if i == 1:
          i=str(i)
          a=(url+page+i+'/')
          r=requests.get(url=a)
          html=r.content
     else:
          i=str(i)
          a=(url+page+i+'/')
          r=requests.get(url=a)
          html1=r.content
          html = html + html1
     #每次间隔1秒
     time.sleep(1)
wp=BeautifulSoup(html,'html.parser')
price=wp.find_all('div','priceInfo')
tp=[]
for a in price:
    totalPrice=a.span.string
    tp.append(totalPrice)
#提取房源信息
houseInfo=wp.find_all('div',attrs={'class':'houseInfo'})
hi=[]
for b in houseInfo:
    house=b.get_text()
    hi.append(house)

#提取房源关注度
followInfo=wp.find_all('div',attrs={'class':'followInfo'})
fi=[]
for c in followInfo:
    follow=c.get_text()
    fi.append(follow)
    
house=pd.DataFrame({'totalprice':tp,'houseinfo':hi,'followinfo':fi})
#查看数据表的内容
house.head()
print(house.head())

