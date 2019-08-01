import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
from time import sleep
from processor import Processor
from config import *

PLATFORM = ''
DEVICE_NAME = ''
APP_PACKAGE = ''
APP_ACTIVITY = ''
DRIVER_SERVER = ''
MONGO_URL = ''
MONGO_DB = ''
MONGO_COLLECTION = ''
SCROLL_SLEEP_TIME = ''
USERNAME = ''
PASSWORD = ''
FLICK_START_X = ''
FLICK_START_Y = ''
FLICK_DISTANCE = ''

class Moments():
    def __init__(self):
        """
        初始化
        """
        # 驱动配置
        self.desired_caps = {
            'platformName': PLATFORM,
            'deviceName': DEVICE_NAME,
            'appPackage': APP_PACKAGE,
            'appActivity': APP_ACTIVITY
        }
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)
        self.wait = WebDriverWait(self.driver, 5)
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]
        self.collection = self.db[MONGO_COLLECTION]
        # 处理器
        self.processor = Processor()

    def login(self):
        """
        登录微信
        :return:
        """
        # 登录按钮
        login = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/d75')))
        login.click()
        # 手机输入
        phone = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/hz')))
        phone.set_text(USERNAME)
        # 下一步
        next = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/alr')))
        next.click()
        # 密码
        password = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/hz"][1]')))
        password.set_text(PASSWORD)
        # 提交
        submit = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/alr')))
        submit.click()
        # 是否查看通讯录
        yesORnot = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/an2')))
        yesORnot.click()

    def enter(self):
        """
        进入朋友圈
        :return:
        """
        # 选项卡
        tab = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/b0w"][3]')))
        tab.click()
        # 朋友圈
        moments = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/a7f')))
        moments.click()

    def crawl(self):
        """
        爬取
        :return:
        """
        while True:
            # 当前页面显示的所有状态
            items = self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//*[@resource-id="com.tencent.mm:id/d58"]//android.widget.FrameLayout')))

            page1 = self.driver.page_source
            # 上滑
            self.driver.swipe(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y)
            # 遍历每条状态
            sleep(2)
            page2 = self.driver.page_source

            if page2 == page1:
                break

            for item in items:
                try:
                    # 昵称
                    nickname = item.find_element_by_id('com.tencent.mm:id/as6').get_attribute('text')
                    # 正文
                    content = item.find_element_by_id('com.tencent.mm:id/ib').get_attribute('text')
                    # 日期
                    date = item.find_element_by_id('com.tencent.mm:id/dfw').get_attribute('text')
                    # 处理日期
                    date = self.processor.date(date)
                    print(nickname, content, date)
                    data = {
                        'nickname': nickname,
                        'content': content,
                        'date': date,
                    }
                    # 插入MongoDB
                    self.collection.update({'nickname': nickname, 'content': content}, {'$set': data}, True)
                    sleep(SCROLL_SLEEP_TIME)
                except NoSuchElementException:
                    pass

    def main(self):
        """
        入口
        :return:
        """
        # 登录
        self.login()
        # 进入朋友圈
        self.enter()
        # 爬取
        self.crawl()


if __name__ == '__main__':
    moments = Moments()
    moments.main()
