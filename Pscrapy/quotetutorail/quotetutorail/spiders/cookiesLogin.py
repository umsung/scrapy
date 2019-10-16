# -*- coding: utf-8 -*-
import time

import scrapy


class CookiesloginSpider(scrapy.Spider):
    name = 'cookiesLogin'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/']
    headers = {}


    def login(self, name, passwd):
        url = 'https://www.zhihu.com/#signin'
        # 这里可以用Chrome、Phantomjs等，如果没有加入环境变量，需要指定具体的位置
        driver = webdriver.Firefox()
        driver.set_window_size(1200, 1200)
        driver.get(url)
        print('开始登录')
        use_passwd_login = driver.find_element_by_class_name('signin-switch-password').click()
        login_button = driver.find_element_by_class_name('active').click()
        name_field = driver.find_element_by_name('account')
        name_field.send_keys(name)
        passwd_field = driver.find_element_by_name('password')
        passwd_field.send_keys(passwd)
        auto_login = driver.find_element_by_xpath('//button[contains(@class,"sign-button")]').click()
        time.sleep(10)
        return driver.get_cookies()

    def set_cookies(self, drive_cookies):
        # 标准化cookies，重新构造
        dict_cookies = {}
        for each in drive_cookies:
            dict_cookies[each['name']] = each['value']
        return dict_cookies

    def start_requests(self):  # 重写start_requets,完成用户登录操作
        # 从登陆页面获取html信息,记住headers传入
        login_name = 'xxxxx'
        login_passwd = 'xxxxxx'
        cookies = self.login(login_name, login_passwd)

        return [scrapy.FormRequest('https://www.zhihu.com/', cookies=cookies, headers=self.headers,
                                   callback=self.after_login)]

    def after_login(self, response):  # 拼接会原有的start_requests
        for url in self.start_urls:
            yield scrapy.Request(url, dont_filter=True, headers=self.headers)  # 默认调用parse


    def parse(self, response):
        pass
