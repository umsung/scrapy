# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:18:51 2018

@author: Administrator
"""

from bs4 import BeautifulSoup
import requests
import json
from multiprocessing  import Pool
from lxml import etree
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}
cookies = {'cookie': 'pgv_pvi=9619568640; PHPSESSID=6cjs500a7ii6bddv6np7nj27l7; pgv_si=s2795575296'}
data_from = {
        
         'spm': '32.779245.4880981.1'
       

    }
     
resp=requests.get('https://www.tangeche.com/market?',params=data_from,headers=headers)
print(resp.url)        
print( resp.text)
# =============================================================================
# soup = BeautifulSoup(resp,'lxml')     
# job_list=soup.find('div',class_="pg-market")
# print(job_list)
# =============================================================================
# ===================================== ========================================
#  
# def parse_html(html):
#     soup=BeautifulSoup(html,'lxml')
#     job_list=soup.select('ul.rob-list > li')
#     print(job_list)
#     for item in job_list:
#         yield {
#                 '图片链接': item.find('img',class_='rob-car-img margin-center').get('href'),
#                 '数量': item.find('p',class_='rob-tag fs22').get('text'),
#                 '车系': item.find('p',class_='car-name text-bold-600').text,            
#                 '品牌': item.find('p',class_='car-info text-bold-600 g-ellipse').text,
#                 '首付': item.find('span',class_='fs24 text-bold-500 payment-num-11-0').text,
#                 '月供': item.find('span',class_='text-bold-400').text
#                 }
# 
# def write_to_file(content):
# # =============================================================================
# #     f=open('bs4s腾讯社招.xls','a',encoding='utf-8',newline='')
# #     w = csv.writer(f)
# #     w.writerow((job_name + job_class))
# # =============================================================================
#     with open('bs4谈个车.xls','a',encoding='utf-8') as f:
#         f.write(json.dumps(content,ensure_ascii=False) +'\n')
#         f.close()
#         
# def main():
#     for item in parse_html(get_html()):
#         print(item)
#         write_to_file(item)
# 
# if __name__=='__main__':
#     main()
# =============================================================================
# =============================================================================
#     pool=Pool()
#     pool.map(main, [10*item for item in range(9)])
# =============================================================================
# =============================================================================
#     for item in range(0,10):
#          main(item*10)
# 
# =============================================================================
