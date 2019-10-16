import requests
import json
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://mall.wine-world.com/')
print(driver.get_cookies())
response = requests.get('https://mmall.wine-world.com/')

print(response.cookies)
print(response.cookies.get_dict())
driver.close()