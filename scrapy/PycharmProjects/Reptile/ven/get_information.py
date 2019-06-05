# -*- coding: utf-8 -*-

import requests #用来访问网页的库，好比浏览器
from bs4 import BeautifulSoup #爬虫库，用来抓取网页中的信息，它有一个可爱的名字beautifulsoup,寓意一碗浓汤，我要从汤中捞出不同的美味
import time
import pandas as pd

def read_url(path):
    path = path
    data = pd.read_csv(path,engine='python')
    try:
        data_received = pd.read_csv('./house_inf_lianjia.csv',engine='python')
        print('导入爬取数据')
        data_received_list = data_received['url'].tolist()
        print('转换表格')
        url_list = data[~data['url'].isin(data_received_list)]['url'].unique().tolist()
        print('剔除已爬取数据')
        print(len(url_list))
    except :
        url_list = data['url'].unique().tolist()
        data = pd.DataFrame(
            columns=['house_id', 'name', 'price', 'area_price', 'area', 'room', 'livingroom', 'kitchenroom',
                     'bathroom', 'lng', 'lat', 'url'])
        data.to_csv('./house_inf_lianjia.csv', encoding='gbk', index=0)
        print('无历史数据')
    return url_list

def save_data():
    data = pd.DataFrame(data_l,columns = ['house_id','name','price','area_price','area','room','livingroom','kitchenroom','bathroom','lng','lat','url'])
    data.to_csv('./house_inf_lianjia.csv',encoding='gbk',index=0,mode='a+',header=False)

def craw_inf(url_list):
    #time.sleep(1)
    headers={
        'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    n = 0
    for url in url_list:
        n += 1
        try:
            web = requests.get(url,headers=headers)
            soup = BeautifulSoup(web.text,'lxml')
            names = soup.select('body > div.sellDetailHeader > div > div > div.title > h1')
            prices = soup.select('body > div.overview > div.content > div.price > span.total')
            area_prices = soup.select('body > div.overview > div.content > div.price > div.text > div.unitPrice > span')
            areas = soup.select('body > div.overview > div.content > div.houseInfo > div.area > div.mainInfo')
            room_types = soup.select('#introduction > div > div > div.base > div.content > ul > li')
            lng = soup.get_text().split("resblockPosition:'")[1].split(',')[0]
            lat = soup.get_text().split("resblockPosition:'")[1].split(',')[1].split("'")[0]
            for name,price,area_price,area,room_type in zip(names,prices,area_prices,areas,room_types):
                #print(name.get_text(),price.get_text(),area_price.get_text(),area.get_text(),room_type.get_text(),lng,lat)
                house_id = url.split('https://sh.lianjia.com/ershoufang/')[1].split('.')[0]
                name = name.get_text()
                price = price.get_text()
                area_price = area_price.get_text().split('元')[0]
                area = area.get_text().split('平')[0]
                room = room_type.get_text().split('房屋户型')[1].split('室')[0]
                livingroom = room_type.get_text().split('室')[1].split('厅')[0]
                kitchenroom = room_type.get_text().split('厅')[1].split('厨')[0]
                bathroom = room_type.get_text().split('厨')[1].split('卫')[0]
                print(house_id,name,price,area_price,area,room,livingroom,kitchenroom,bathroom,lng,lat)
                data_l.append([house_id,name,price,area_price,area,room,livingroom,kitchenroom,bathroom,lng,lat,url])
                if n % 10 ==0 :
                    print('save')
                    save_data()
                    data_l.clear()
                else:
                    print('continue')
        except:

            print('error pass')
        

if __name__ == '__main__':
    url_list = read_url('./urls.csv')
    data_l = []
    craw_inf(url_list)

