# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:08:52 2018

@author: Administrator
"""
import urllib.request
import http.cookiejar

#cookie
cookie=http.cookiejar.CookieJar()
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('http://www.wine-world.com.hk/')
print(response.read().decode('utf-8'))
for item in cookie:
    print(item.name+"="+item.value)
    
# #代理ip
# proxy_handler=urllib.request.ProxyHandler(
#         {
#                 'http': 'http://127.0.0.1:9743',
#                 'https': 'https://127.0.0.1:9743'
#                 }
#         )
# opener=urllib.request.build_opener(proxy_handler)
# response=opener.open('www.baidu.com/')
# print(response.read())