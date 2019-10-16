import requests
from bs4 import BeautifulSoup
import re
import base64
import io
from lxml import etree
from fontTools.ttLib import TTFont
#网页下载
def Get_page(url):
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'} 
    pages =requests.get(url, headers=headers)
    return pages.text

# 爬取信息 
def Get_info(html):
    soup = BeautifulSoup(html,'html.parser',)
    cons = soup.find('ul',class_='house-list').find_all('li') 
    for con in cons: 
        try:
            names = con.find('a',class_='strongbox').string.replace(' ','') 
            kinds = con.find('p',class_='room').string.replace(' ','') 
            money = con.find(class_='money').find('b').string.replace(' ','')
        except: 
            pass

        print(names+'\n'+kinds+'\n'+money)

def main():
    url = 'https://nj.58.com/jiangning/chuzu/0/?PGTID=0d3090a7-000a-cd8d-23ec-74b8f4ad6119&ClickID=2'
    response_= Get_page(url)
    if '访问过于频繁，本次访问做以下验证码校验' in response_:
        print('验证码出现！')
    # print(response_)
#获取加齒字符串_
    base64_str=re.search(r"base64,(.*?)'\)",response_, re.S).group(1)
    # print(base64_str)
    b = base64.b64decode(base64_str)
    print(b.decode('UTF-8'))
    print(io.BytesIO(b))
    # BytesIO实现了在内存中读写bytes
    font = TTFont(io.BytesIO(b))
    print(font)
    bestcmap = font['cmap'].getBestCmap()
    print(bestcmap)
    newmap  = dict()
    for key in bestcmap.keys():
        value = int(re.search(r'(\d+)', bestcmap[key]).group(1))-1
        print(value) 
        key = hex(key) 
        print(key)
        newmap[key] = value 
#把页面上自定义字体替换成正常字体
    for key,value in newmap.items():
        key_ = key.replace('0x','&#x') + ';'
        if key_ in response_:
            response_ = response_.replace(key_,str(value))
    # Get_info(response_)

if __name__ == "__main__":
    main()