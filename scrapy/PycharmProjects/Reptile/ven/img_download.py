# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 13:47:03 2018

@author: Administrator
"""
import requests
import re
import urllib.request
from urllib.request import urlopen

def get_html(url):
    respose=requests.get(url)
    if respose.status_code==200:
        html=respose.text
        return html

def get_img(html):
    img_url=re.findall(r'class="BDE_Image".*?src="(.*?)"',html,re.S)
    x=0
    for src in img_url:
       urllib.request.urlretrieve(src, '%s.jpg' %x)             
       x += 1
       
def __main__():       
    for i in range(4,5):
       url='https://tieba.baidu.com/p/1753935195?red_tag=261988075%d'%i
       code=get_html(url)
       get_img(code)
    
if __name__ == '__main__':
       __main__()    
