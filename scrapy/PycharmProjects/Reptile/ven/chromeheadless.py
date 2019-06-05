# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 16:37:57 2018

@author: Administrator
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.aliyun.com/jiaocheng/124644.html")
content = driver.page_source
print(content)
driver.quit()
