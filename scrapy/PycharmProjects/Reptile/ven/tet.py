# coding:utf-8
from selenium import webdriver
from selenium.common.exceptions import *   # 导入所有的异常类
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Yoyo(object):
    """基于原生的selenium框架做了二次封装."""
    def __init__(self):
        """启动浏览器参数化，默认启动firefox."""
        self.driver = webdriver.Chrome()

    def get(self, url):
        '''使用get打开url'''
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        # ‘‘‘定位元素方法封装‘‘‘
        element = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(locator))
        return element

    def click(self, locator):
        # ‘‘‘点击操作‘‘‘
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        # ‘‘‘发送文本，清空后输入‘‘‘
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

if __name__ == "__main__":
    d = Yoyo()  # 启动firefox
    d.get("https://www.baidu.com")
    input_loc = ("id", "kw")
    d.send_keys(input_loc, "yoyo")   # 输入搜索内容
    button_loc = ("id", "kw")
    d.click(button_loc)           # 点击搜索按钮