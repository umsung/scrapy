# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:03:08 2018

@author: Administrator
"""

import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from hashlib import md5
import os
from lxml import etree

html = requests.get('http://glidedsky.com/login')
selector = etree.HTML(html.text)
_token = selector.xpath('//*[@id="app"]/main/div/div/div/div/div[2]/form/input/@value')[0]
print(_token)

data = {
    '_token': _token,
    'email': '3238321252@qq.com',
    'password': '821874169'
}
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
    'Cookie': '_ga=GA1.2.1884163979.1558064145; _gid=GA1.2.443599804.1558064145; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1558064145; XSRF-TOKEN=eyJpdiI6IndTbFk5ZEN5MmYxbHBHbjBhNmF4bVE9PSIsInZhbHVlIjoid3ozMllUN2dZekNDZ3BcLzROc2tvNHFXOGtoV0puNnIrVGpvNVhuMjMyWFpNZ3lcLzVtMzNYMkljdXlZT0F3ejRFIiwibWFjIjoiOTFmZjg3YjE5MDg2ZTA0ODczZDQxYWM2OGViODQ2ZTEyNjJkN2Q5NmIwNTgxOTcxNDc0NzU2NDZkNWNlZTYxNiJ9; glidedsky_session=eyJpdiI6IjBNQmRYSmRPbEdlXC9WdnZadWZSXC9EQT09IiwidmFsdWUiOiJQOTluMTFuUFFUdkROWVZ0a1wvUHluZjkwdzQ3UTd5eE1SVENUMnpTNCtxc3pzdUdJM3VYbm5sTkladlk4RGN2USIsIm1hYyI6ImVkZTcxMTIzNTc1YjdhMmI5NTk3Y2E5ZWJkNDAwMjljMjE3NThhYWMxMjZjNTM3YjY4NmRiMjVkZmNlY2NlMTMifQ%3D%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1558081715',
    'Content-Type': 'application/x-www-form-urlencoded'
  }

s = requests.session()
resp = s.post(url='http://glidedsky.com/login', data=data, headers=header)
print(resp.status_code)
print(resp.text)
print(resp.cookies.get_dict())
# a = s.get(url = 'http://glidedsky.com/api/level/web/crawler-javascript-obfuscation-1/items?page=3&t=1558076927&sign=898aef21d4e9e1c2dd71f36468aa49d108c04afd', verify = False)
# print(a.text)
# headers = {
#     'Host': 'glidedsky.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
#     'Cookie': '_ga=GA1.2.1884163979.1558064145; _gid=GA1.2.443599804.1558064145; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1558064145; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IitVQUJhSWtvcU1PamJhMXJQa0ZTM1E9PSIsInZhbHVlIjoiNUk1Z0hwdUdxUHE1ZWRJaEJ1bTlNRnZWQm55d1dPK0M2Y1ZWREZ5R1hRVzJTdVpJUXJibVBsUlp2XC8zcHExNjNGaFBSbEdRRlRKYzI3NGhaOTF3K2VhYm1CWE80M083V0syWWRGZGIreU9TVHJMV3g0dGtSNGFYXC9cL1E5WmhpK2QzQndmSGZrZkxoQXBaTCsrVkhNQzhSU0pGQytvZXZvOVl4Yk5Kc1wvb0VCTT0iLCJtYWMiOiJlZGZkYjE2YmM0NTM5YTk2ZjM0OWQ0ZTAxYTNmYzhmZjZkMTczYWQ3OGRlNzg5NTYyZTJlNjE1NTc1NmY2NTkzIn0%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1558076902; _gat_gtag_UA_75859356_3=1; XSRF-TOKEN=eyJpdiI6IlFTbzJUSGFEUkJsVkNuTjlHcXJZUnc9PSIsInZhbHVlIjoiQTZWWGk4eEFqUnhrVVZXd29lb3dHejBCSWgrMXR5QXRXZzdibWxBYWxmSStCNUt1TThiY21HSDhzK0dkRWcrWSIsIm1hYyI6ImM0NGM1M2Q1ZTExOTA2ZTRhNDhiNzc0Y2ZiZGM5ZjBmMjk2ZTM0Njk1N2Q3MGU5N2Q2NTNhYzYxNzgyOTM4NzMifQ%3D%3D; glidedsky_session=eyJpdiI6InpYc2lhaEtreERhSFExdnJvWWcrY0E9PSIsInZhbHVlIjoiR0ZJWFZzV2E5QVhcL3kzZmdzbWh0XC9DTzNSZHgwZ0x6UHJ5WHlDNk52dmRJc0ZyUWZSRlp1d09mV2lWXC9BbHk2UyIsIm1hYyI6ImY2NmQ3NTAwNWY5ZDk1NjkzZjgxMmNlM2I5ZTQxZjllYzgxZTdiNTNjOTM1ZDgyMTA5ODNmNGMyNGMxMzA0M2QifQ%3D%3D',
#     'Connection': 'keep-alive',
#     'Accept': '*/*',
#     'X-Requested-With': 'XMLHttpRequest',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Referer': 'http://glidedsky.com/level/web/crawler-javascript-obfuscation-1?page=3'
#   }
#
#
# Cookie= '_ga=GA1.2.1884163979.1558064145; _gid=GA1.2.443599804.1558064145; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1558064145; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IitVQUJhSWtvcU1PamJhMXJQa0ZTM1E9PSIsInZhbHVlIjoiNUk1Z0hwdUdxUHE1ZWRJaEJ1bTlNRnZWQm55d1dPK0M2Y1ZWREZ5R1hRVzJTdVpJUXJibVBsUlp2XC8zcHExNjNGaFBSbEdRRlRKYzI3NGhaOTF3K2VhYm1CWE80M083V0syWWRGZGIreU9TVHJMV3g0dGtSNGFYXC9cL1E5WmhpK2QzQndmSGZrZkxoQXBaTCsrVkhNQzhSU0pGQytvZXZvOVl4Yk5Kc1wvb0VCTT0iLCJtYWMiOiJlZGZkYjE2YmM0NTM5YTk2ZjM0OWQ0ZTAxYTNmYzhmZjZkMTczYWQ3OGRlNzg5NTYyZTJlNjE1NTc1NmY2NTkzIn0%3D; _gat_gtag_UA_75859356_3=1; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1558077867; XSRF-TOKEN=eyJpdiI6IlFCN28wUXFsWmJXMmZtek92cHRKb2c9PSIsInZhbHVlIjoic2dzNlBRaVN0STJyWEh2eWF0TnFibGZoRms0ZkNoQmtPWjZZWUxiY1BIRklSNmpCR1Y0THJPZkozMXZaNHU2VCIsIm1hYyI6IjhkYzA5MWMwNzkyMWUxNjgwYmYwMTJiNGNjMDg4Y2E0M2Y1OTkyMmQxZjUxYTQ3MjM5NGE3YzAxZTgzOTQyNjYifQ%3D%3D; glidedsky_session=eyJpdiI6InppTFA5cnpLWlFiT1VMd28xS2Y5anc9PSIsInZhbHVlIjoiQXJGVCtuVUxFS243YjFTUW9cL2JtZ1ZQdGpueXJDK0tcL3BjWjdXTzRNb1ZvbU9jeGxRR3cxc0tnN3duYXdGVUZ6IiwibWFjIjoiYjQzOTJiYzc3OTNkNWQzNDkxYzkxZTFmYzg1MGFiZDA4NDAxZTg2ODYzODA2YzdjN2Y5ZTkyMmI1M2ZkYzVkMiJ9'
# Cookie_dict = {i.split('=')[0]: i.split('=')[1] for i in Cookie.split(';')}
#
# url = 'http://glidedsky.com/api/level/web/crawler-javascript-obfuscation-1/items?page=3&t=1558076927&sign=898aef21d4e9e1c2dd71f36468aa49d108c04afd'
# urll = 'http://glidedsky.com/api/level/web/crawler-javascript-obfuscation-1/items'
#
#
# resp = s.get(url, headers=headers, cookies=cookie)
# print(s.cookies.get_dict())
# #resp.encoding='utf-8'
# try:
#     print(resp.status_code)
#     if resp.status_code == 200:
#         result = resp.text
# #        html = resp.content.decode(resp.apparent_encoding)
#         print(result)
#
# except ConnectionError:
#     pass