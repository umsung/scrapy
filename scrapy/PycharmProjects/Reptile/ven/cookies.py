# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 11:00:26 2018

@author: Administrator
"""

import urllib.request
import http.cookiejar

#/*设置文件来存储Cookie*/
filename = 'cookie.txt'
#/*创建一个MozillaCookieJar()对象实例来保存Cookie*/
cookie = http.cookiejar.MozillaCookieJar(filename)
#/*创建Cookie处理器*/
handler = urllib.request.HTTPCookieProcessor(cookie)
#/*构建opener*/
opener = urllib.request.build_opener(handler)
response = opener.open("https://www.douban.com/")
cookie.save(ignore_discard=True, ignore_expires=True)

