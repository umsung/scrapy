# -*- coding: utf-8 -*-

import requests 
from bs4 import BeautifulSoup 
import time 
import pandas as pd

def create_url(area_max,cat):
    urls = 'https://sh.lianjia.com/ershoufang/ba{}ea{}/'
    num = 0
    url_list = []

    for i in range(int(area_max/cat)):
        url_list.append(urls.format(num,num+cat))
        num += cat
    url_list.append(urls.format(area_max,area_max*100))
    return url_list

def craw_second_url(url_list):
    print(url_list)
    #data_list = []
    headers={
            'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    for url in url_list:
        print(url)
        url_start = requests.get(url,headers=headers)
        soup = BeautifulSoup(url_start.text,'lxml')
        house_sum = soup.select('body > div.content > div.leftContent > div.resultDes.clear > h2 > span')
        for house in house_sum:
            house_number = int(house.get_text())
            page_numbers = house_number/30
        if page_numbers == 0:
            page_num = 0
        elif page_numbers>=100:
            page_num = 100
        else:
            page_num = int(page_numbers)+1
        print(page_num)
        final_url = url.split('ba')
        final_url = final_url[0]+'pg{}ba'+final_url[1]
        if page_num== 0:
            pass
        else:
            for page in range(1,page_num+1):
                print(page)
                u = final_url.format(page)
                print(u)
                url_data = requests.get(u,headers=headers)
                soup = BeautifulSoup(url_data.text,'lxml')
                url_all = soup.select('body > div.content > div.leftContent > ul > li > div.info.clear > div.title > a')
                for u_data in url_all:
                    hf = u_data.get('href')
                    print(hf)
                    data_list.append(hf)
        #time.sleep(1)#爬虫间隔时间设置
    return data_list
                    
if __name__=='__main__':                 
    url_list = create_url(220,2) #填写区间最大面积和公差，保证按大于最大面积搜索，房源数小于等于3000
    data_list = []
    #data_list = craw_second_url(url_list)
    craw_second_url(url_list)
    data =  pd.DataFrame(pd.Series(data_list),columns=['url'])
    data.to_csv('./urls.csv',encoding='gbk',index=0)
    print('finish')







