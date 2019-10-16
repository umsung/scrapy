from selenium import webdriver
import time


class ClassA(object):

    def open_baidu(self):
        driver = webdriver.Chrome()
        driver.get('https://www.baidu.com')
        driver.maximize_window()
        time.sleep(1)
        driver.quit()