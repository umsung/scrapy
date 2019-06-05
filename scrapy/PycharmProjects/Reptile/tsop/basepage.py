import os, time
from tsop.logger import *


MyLogger = Logger('BasePage').get_log()


class BasePage(object):
    """
 主要是把常用的几个Selenium方法封装到BasePage这个类，我们这里演示以下几个方法
    selenium二次封装
    back()
    forward()
    get()
    quit()
    """
    def __init__(self, driver):
        """
         写一个构造函数，有一个参数driver
         :param driver:
         """
        self.driver = driver

    def back(self):
        self.driver.back()
        MyLogger.info('返回')

    def forward(self):
        self.driver.forward()
        MyLogger.info('前进')


    def open_url(self, url):
        self.driver.get(url)
        MyLogger.info('打开')


    def quit_browser(self):
        self.driver.quit()
        MyLogger.info('退出')


    def take_screenshot(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '/Screenshots/'
        print(file_path)
        print(os.path.dirname(os.getcwd()) + '/Screenshots/')
        sj = time.strftime('%y%m%d%H%M%S', time.localtime())
        screen_name = file_path + sj + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            MyLogger.info('开始截图保存')
        except Exception as e:
            MyLogger.error('出错', format(e))



