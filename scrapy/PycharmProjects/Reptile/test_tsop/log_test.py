from tsop.logger import *
import time
from selenium import webdriver

mylogger = Logger('TestLog').get_log()


class MyLogger(object):

    def print_log(self):
        driver = webdriver.Chrome()
        mylogger.info('打开浏览器')

        driver.maximize_window()
        mylogger.info('浏览器窗口最大化')

        driver.get('https://www.baidu.com')
        mylogger.info('打开百度首页。')

        time.sleep(1)
        mylogger.info('停一秒钟')

        driver.quit()
        mylogger.info('关闭')


testlog = MyLogger()
testlog.print_log()