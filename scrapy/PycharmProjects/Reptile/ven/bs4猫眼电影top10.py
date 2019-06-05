# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 11:42:54 2018

@author: Administrator
"""
from bs4 import BeautifulSoup
import requests
import json
from multiprocessing  import Pool

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}
cookies = {'cookie': 'pgv_pvi=9619568640; PHPSESSID=6cjs500a7ii6bddv6np7nj27l7; pgv_si=s2795575296'}

def get_html(url):
    try:
        
        resp=requests.get(url,headers=headers)
        if resp.status_code==200:
            return resp.text
        return None
    except ConnectionError:
        print("error occured")
        return None

 
def parse_html(html):
    soup=BeautifulSoup(html,'lxml')
    job_list=soup.select('dl.board-wrapper > dd')
    print(job_list)
    for item in job_list:
        yield {
                '链接': 'http://maoyan.com'+ item.find('a',class_='image-link').get('href'),
                '名称': item.find('a',class_='image-link').get('title').strip()[:3],
                '主演': item.find('p',class_='star').text.strip()[:3],            
                '时间': item.find('p',class_='releasetime').text,
                '评分': item.find('i',class_='integer').text + item.find('i',class_='fraction').text,
                '图片': item.find('img',class_='board-img').get('data-src')
                }

def write_to_file(content):
# =============================================================================
#     f=open('bs4s腾讯社招.xls','a',encoding='utf-8',newline='')
#     w = csv.writer(f)
#     w.writerow((job_name + job_class))
# =============================================================================
    with open('bs4猫眼电影.xls','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False) +'\n')
        f.close()
        
def main(num):
    url='http://maoyan.com/board/4?offset='+ str(num)
    html=get_html(url)
    for item in parse_html(html):
        print(item)
        write_to_file(item)

if __name__=='__main__':
    
    pool=Pool()
    pool.map(main, [10*item for item in range(9)])
# =============================================================================
#     for item in range(0,10):
#          main(item*10)
# 
# =============================================================================
