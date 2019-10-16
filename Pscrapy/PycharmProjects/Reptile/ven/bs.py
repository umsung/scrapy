# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 11:06:51 2018

@author: Administrator
"""

from bs4 import BeautifulSoup
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}
cookies = {'cookie': 'pgv_pvi=9619568640; PHPSESSID=6cjs500a7ii6bddv6np7nj27l7; pgv_si=s2795575296'}
resp=requests.get('http://maoyan.com/board/4?offset=0',headers=headers)
html=resp.text
soup=BeautifulSoup(html,'lxml')
job_list=soup.select('dl.board-wrapper > dd')
print(job_list)
