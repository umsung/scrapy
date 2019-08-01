# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:12:52 2019

@author: Administrator
"""

from selenium import webdriver
import random
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import requests

driver=webdriver.Chrome()
wait = WebDriverWait(driver,10)
driver.get("http://baidu.com/")
driver.get("http://mall.wine-world.com/")

print(driver.get_cookies())
# [{'domain': '.wine-world.com', 'expiry': 1592462361, 'httpOnly': False, 'name': 'SIDDAB555555', 'path': '/', 'secure': False, 'value': '6907de8d4ceb42fa8b780ca6af137275'}, {'domain': '.wine-world.com', 'httpOnly': True, 'name': 'ASP.NET_SessionId', 'path': '/', 'secure': False, 'value': '2wegpmhzzibpojcs2megcoq3'}, {'domain': '.wine-world.com', 'expiry': 1592462358, 'httpOnly': False, 'name': 'PIDDAB555555', 'path': '/', 'secure': False, 'value': '2019061914391653797894'}, {'domain': '.wine-world.com', 'expiry': 1592462361, 'httpOnly': False, 'name': 'VPSDAB555555', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.wine-world.com', 'expiry': 1592462361, 'httpOnly': False, 'name': 'FVTDAB555555', 'path': '/', 'secure': False, 'value': '636965519593817234'}, {'domain': '.wine-world.com', 'expiry': 1592462361, 'httpOnly': False, 'name': 'LVTDAB555555', 'path': '/', 'secure': False, 'value': '636965519593817234'}, {'domain': '.wine-world.com', 'expiry': 1560926368, 'httpOnly': False, 'name': 'HBCDAB555555', 'path': '/', 'secure': False, 'value': '%7B%22Ticks%22%3A%22636965519601629734%22%2C%22haschat%22%3Afalse%2C%22vstatus%22%3A1%2C%22startkind%22%3A1%2C%22lroid%22%3A%22%22%2C%22oname%22%3A%22%22%2C%22Result%22%3A%22%22%2C%22cos%22%3A%22%22%2C%22pc%22%3A%22dedd1411a524492481508fb405c0a8e1%22%7D'}, {'domain': '.wine-world.com', 'expiry': 1592462361, 'httpOnly': False, 'name': 'MSTSDAB555555', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.wine-world.com', 'expiry': 1592462361, 'httpOnly': False, 'name': 'VTSDAB555555', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.mall.wine-world.com', 'expiry': 1592462364, 'httpOnly': False, 'name': 'Hm_lvt_620cf839bf33348a27b35148221312d0', 'path': '/', 'secure': False, 'value': '1560926363'}, {'domain': '.mall.wine-world.com', 'httpOnly': False, 'name': 'Hm_lpvt_620cf839bf33348a27b35148221312d0', 'path': '/', 'secure': False, 'value': '1560926363'}, {'domain': '.wine-world.com', 'httpOnly': False, 'name': 'un', 'path': '/', 'secure': False, 'value': 'none'}, {'domain': '.wine-world.com', 'expiry': 1592462365.314519, 'httpOnly': True, 'name': 'wine.account', 'path': '/', 'secure': False, 'value': 'ae830bc6-e3d0-4768-a0b7-21159e7b6a18'}]


h=driver.current_window_handle
driver.maximize_window()
phoneNum = 19900000353
name = '杨智'

#登陆
signInBut = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="currentAccount_Div"]/a[1]')))
signInBut.click()
#driver.find_element_by_xpath("//*[@class='box']/div[2]/a[1]").click()
driver.find_element_by_xpath("//*[@id='UserName']").send_keys(phoneNum)
time.sleep(0.1)
driver.find_element_by_xpath("//*[@id='PassWord']").send_keys("123456")
time.sleep(0.1)
driver.find_element_by_xpath("//*[@id='loginSubmit']").click()

print(driver.get_cookies())

# [{'domain': '.wine-world.com', 'expiry': 1592462380, 'httpOnly': False, 'name': 'SIDDAB555555', 'path': '/', 'secure': False, 'value': '6907de8d4ceb42fa8b780ca6af137275'}, {'domain': '.wine-world.com', 'httpOnly': True, 'name': 'ASP.NET_SessionId', 'path': '/', 'secure': False, 'value': '2wegpmhzzibpojcs2megcoq3'}, {'domain': '.wine-world.com', 'expiry': 1592462358, 'httpOnly': False, 'name': 'PIDDAB555555', 'path': '/', 'secure': False, 'value': '2019061914391653797894'}, {'domain': '.wine-world.com', 'httpOnly': True, 'name': 'WINE.AUTH', 'path': '/', 'secure': False, 'value': '55C83DFDBCC9AB213A34E6A5149EFBCC7A938DD01D2FEDD0A7378A0A233048CCF9202BB7F2559A8BC37275852C38A3D983B1471A39792261A8CB6201867B628DF45712F85B70C23990B8828A1FA6E77B23F8F24989BFB6E28559FD1B36D92BC0BF151F09'}, {'domain': '.wine-world.com', 'expiry': 1592462361, 'httpOnly': False, 'name': 'FVTDAB555555', 'path': '/', 'secure': False, 'value': '636965519593817234'}, {'domain': '.wine-world.com', 'expiry': 1592462361, 'httpOnly': False, 'name': 'LVTDAB555555', 'path': '/', 'secure': False, 'value': '636965519593817234'}, {'domain': '.wine-world.com', 'expiry': 1592462375.69075, 'httpOnly': True, 'name': 'wine.account', 'path': '/', 'secure': False, 'value': '61094f42-614f-4b00-96b4-f48f8cfaa7e7'}, {'domain': '.wine-world.com', 'expiry': 1592462361, 'httpOnly': False, 'name': 'MSTSDAB555555', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.wine-world.com', 'expiry': 1592462361, 'httpOnly': False, 'name': 'VTSDAB555555', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.wine-world.com', 'expiry': 1592462380, 'httpOnly': False, 'name': 'VPSDAB555555', 'path': '/', 'secure': False, 'value': '3'}, {'domain': '.wine-world.com', 'httpOnly': False, 'name': 'un', 'path': '/', 'secure': False, 'value': '19900000353'}, {'domain': '.wine-world.com', 'expiry': 1560926386, 'httpOnly': False, 'name': 'HBCDAB555555', 'path': '/', 'secure': False, 'value': '%7B%22Ticks%22%3A%22636965519791160984%22%2C%22haschat%22%3Afalse%2C%22vstatus%22%3A1%2C%22startkind%22%3A1%2C%22lroid%22%3A%22%22%2C%22oname%22%3A%22%22%2C%22Result%22%3A%22%22%2C%22cos%22%3A%22%22%2C%22pc%22%3A%22da58b94201634645934de010b64e361b%22%7D'}, {'domain': '.mall.wine-world.com', 'expiry': 1592462381, 'httpOnly': False, 'name': 'Hm_lvt_620cf839bf33348a27b35148221312d0', 'path': '/', 'secure': False, 'value': '1560926363,1560926381'}, {'domain': '.mall.wine-world.com', 'httpOnly': False, 'name': 'Hm_lpvt_620cf839bf33348a27b35148221312d0', 'path': '/', 'secure': False, 'value': '1560926381'}]

cookies = driver.get_cookies()

driver.delete_all_cookies()

#  selenium添加cookies，域名需要和当前网址一致。否则会报错  driver.get_cookies()
a=[]
for i in cookies:
    if i['domain'][1:] in driver.current_url:
        a.append(i)

time.sleep(1)
driver.get("http://mall.wine-world.com/")

for x in a:
    driver.add_cookie(x)
time.sleep(1)
driver.refresh()


#  reuqest添加cookies，只需要cookies的键和值， requests.cookies.get_dict()

cookies1 = {}
for b in cookies:
    cookies1[b['name']] = b['value']

resp = requests.get('http://mall.wine-world.com/', cookies=cookies1)
# print(resp.text)

