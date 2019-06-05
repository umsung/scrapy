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
driver.get("http://mall.wine-world.com/")
print(driver.get_cookies())

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

cookies = driver.get_cookies()

driver.delete_all_cookies()

a=[]
cookies1 = {}
for i in cookies:
    if i['domain'][1:] in driver.current_url:
        a.append(i)

for b in cookies:
    cookies1[b['name']] = b['value']

time.sleep(1)
driver.get("http://mall.wine-world.com/")

for x in a:
    driver.add_cookie(x)
time.sleep(1)
driver.refresh()

resp = requests.get('http://mall.wine-world.com/', cookies=cookies1)
print(resp.text)

