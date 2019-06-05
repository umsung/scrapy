from selenium import webdriver
from automation_framework_demo.framework.logger import *
import os
import time
import configparser

logger = Logger('BrowserEngine').getlog()


class BrowserEngine(object):

    dir = os.path.dirname(os.path.abspath('.'))
    firefox_path = dir + '/tools/geckodriver.exe'

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        config = configparser.ConfigParser()
        config_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        # print(config_path)
        config.read(config_path, encoding='utf-8')

        browser = config.get('browser_type', 'browser_name')
        logger.info('获取浏览器类型 %s' % browser)

        url = config.get('testServer', 'URL')
        logger.info('获取打开的网址 %s' % url)

        if browser == 'Chrome':
            driver = webdriver.Chrome()
            logger.info('浏览器类型 %s' % browser)

        elif browser == 'Firefox':
            driver = webdriver.Firefox(self.firefox_path)
            logger.info('浏览器类型 %s' % browser)

        elif browser == 'IE':
            driver = webdriver.Ie()
            logger.info('浏览器类型 %s' % browser)

        driver.get(url)
        logger.info('打开网址 %s' % url)

        driver.maximize_window()
        logger.info('窗口最大化')

        driver.implicitly_wait(10)
        logger.info('Set implicitly wait 10 seconds.')
        return driver

    def browser_quit(self):
        logger.info("Now, Close and quit the browser.")

        self.driver.quit()


