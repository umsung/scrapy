from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pymongo import MongoClient
from selenium.webdriver.common.by import By

class Appium(object):
    def __init__(self):
        self.desired_caps = {'platformName': 'Android',     # 这里是android的apk
                             'deviceName': 'emulator-5554',   # 手机设备名称，通过adb devices查看
                             'platformVersion': '5.3.5',  # android系统的版本号
                             'appPackage': 'com.keruiyun.redwine',
                             'noReset': '!!bool True',   # 不重置app
                             'uuid': 'emulator-5554',   # adb devices查看到的前面那一串
                             'appActivity': 'com.keruiyun.redwine.MainActivity'}

        self.driver = webdriver.Remote('https://127.0.0.1:0000/wd/hub', self.desired_caps)
        self.wait = WebDriverWait(self.driver, 5)
        self.client = MongoClient('localhost')
        self.db = self.client['db_name']
        self.table = self.db['table_name']

    def login(self):
        print(self.driver.contexts)

        # 等待页面页面activity加载完全
        self.driver.wait_activity(self.driver.current_activity, 2)

        login_page = self.wait.until(EC.presence_of_element_located((By.XPATH, ''))).click()