# -*- coding: utf-8 -*-
import re
import datetime

try:
    import urlparse as parse
except:
    from urllib import parse

import scrapy
from selenium import webdriver
import time


class ZhihuSpider(scrapy.Spider):
    name = "zhihuSelenium"
    allowed_domains = ["www.zhihu.com"]
    start_urls = ['https://www.zhihu.com/']
    login_cookies = []

    headers = {
        "HOST": "www.zhihu.com",
        "Referer": "https://www.zhizhu.com",
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
    }

    # selenium登录保存cookies
    def get_cookies(self):
        browser = webdriver.Chrome(executable_path="C:/Program Files/Google/Chrome/Application/chromedriver.exe")
        time.sleep(2)  # 延时为了让页面加载完

        browser.get("https://www.zhihu.com/#signin")
        # browser.find_element_by_css_selector(".qrcode-signin-cut-button").click()
        # browser.find_element_by_css_selector(".signup-social-buttons").click()
        # browser.find_element_by_css_selector(".js-bindweibo").click()
        # browser.switch_to.window(browser.window_handles[-1])
        browser.find_element_by_css_selector("#root > div > main > div > div > div > div.SignContainer-inner > div.Login-content > form > div.SignFlow-account > div.SignFlowInput.SignFlow-accountInputContainer > div.SignFlow-accountInput.Input-wrapper > input").send_keys("xxx")
        browser.find_element_by_css_selector("#root > div > main > div > div > div > div.SignContainer-inner > div.Login-content > form > div.SignFlow-password > div > div.Input-wrapper > input").send_keys("xxx")
        browser.find_element_by_css_selector("#root > div > main > div > div > div > div.SignContainer-inner > div.Login-content > form > button").click()
        time.sleep(2)  # 延时为了让页面加载完
        browser.find_element_by_css_selector("a[node-type='submit']").click()
        login_cookies = browser.get_cookies()
        browser.close()

    # 第一步:先于parse方法执行，处理登陆逻辑。可以猜测，start_requests携带的cookie会给后续所有的访问自动带上
    def start_requests(self):
        return [scrapy.Request('https://www.zhihu.com/#signin', headers=self.headers, cookies=self.login_cookies,
                               callback=self.parse)]

    # 第二步:处理登陆后的逻辑
    def parse(self, response):
        my_url = 'https://www.zhihu.com/people/edit'  # 该页面是个人中心页，只有登录后才能访问
        yield scrapy.Request(my_url, headers=self.headers)