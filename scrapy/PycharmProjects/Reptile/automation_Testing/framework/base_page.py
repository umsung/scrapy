from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from framework.logger import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logger = Logger('BasePage').getlog()


class BasePage(object):
    """
        定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        """
         写一个构造函数，有一个参数driver
         :param driver:
         """
        self.driver = driver

    def back(self):
        self.driver.back()
        logger.info('返回')

    def forward(self):
        self.driver.forward()
        logger.info('Click forward on current page.')

    def open_url(self, url):
        self.driver.get(url)
        logger.info('打开')

    def quit_browser(self):
        self.driver.quit()
        logger.info('退出')

    def implicitly_wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info('wait for %d seconds' % seconds)

    # def driver_wait(self):
    #     wait = WebDriverWait(self.driver, 15)
    #     return wait

    def expected_conditions(self, *locator):
        try:
            wait = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(*locator))
            return wait
        except TimeoutError:
            self.get_windows_img()
            return self.expected_conditions()

    def close(self):
        try:
            self.driver.close()
            logger.info('Closing and quit the browser.')
        except NameError as e:
            logger.info('Failed to quit the browser with %s' % e)

    def current_url(self):
        return self.driver.current_url

    # 获取浏览器驱动
    def get_driver(self):
        return self.driver

    # 执行js脚本
    def execute(self, js, *args):
        self.driver.execute_script(js, *args)

    # 移动到指定元素
    def move_to(self, *args):
        ActionChains(self.driver).move_to_element(self.find_element(*args)).perform()

    # 切换frame页面
    def switch_to_frame(self, param):
        self.driver.switch_to.frame(param)

    # 切换alter
    def switch_to_alert(self):
        return self.driver.switch_to.alert

    # 获取网页标题
    def get_page_title(self):
        logger.info('Current page title is %s' % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info('sleep for %d seconds' % seconds)

    def get_windows_img(self):
        path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        sj = time.strftime('%y%m%d%H%M%S', time.localtime())
        img_name = path + sj + '.png'
        try:
            self.driver.get_screenshot_as_file(img_name)
            logger.info('Had take screenshot and save to folder : /screenshots')
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    def current_window(self):
        return self.driver.current_window_handle

    def window_handles(self):
        return self.driver.window_handles

    def switch_to(self, num):
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[num])

    # 切换窗口
    def switch_to_window(self, partial_url='', partial_title=''):
        """切换窗口
            如果窗口数<3,不需要传入参数，切换到当前窗口外的窗口；
            如果窗口数>=3，则需要传入参数来确定要跳转到哪个窗口
        """
        all_windows = self.driver.window_handles
        if len(all_windows) == 1:
            logger.warning('只有1个window!')
        elif len(all_windows) == 2:
            other_window = all_windows[1 - all_windows.index(self.current_window)]
            self.driver.switch_to.window(other_window)
        else:
            for window in all_windows:
                self.driver.switch_to.window(window)
                if partial_url in self.driver.current_url or partial_title in self.driver.title:
                    break
        logger.debug(self.driver.current_url, self.driver.title)

    # 寻找指定元素
    def find_element(self, *args):
        return self.driver.find_element(*args)

    # 寻找指定的一批元素
    def find_elements(self, *args):
        return self.driver.find_elements(*args)

    def isElementExist(self, *args):
        a = self.find_elements(*args)
        if len(a) == 0:
            return False
        elif len(a) == 1:
            return True
        else:
            return False

    # 定位元素方法
    # def find_element(self, selector):
    #     """
    #      这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
    #      submit_btn = "id=>su"
    #      login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
    #      如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
    #     :param selector:
    #     :return: element
    #     """
    #     element = ''
    #     if '=>' not in selector:
    #         return self.driver.find_element_by_id(selector)
    #     selector_by = selector.split('=>')[0]
    #     selector_value = selector.split('=>')[1]
    #
    #     if selector_by == "i" or selector_by == 'id':
    #         try:
    #             element = self.driver.find_element_by_id(selector_value)
    #             logger.info("Had find the element \' %s \' successful "
    #                         "by %s via value: %s " % (element.text, selector_by, selector_value))
    #         except NoSuchElementException as e:
    #             logger.error("NoSuchElementException: %s" % e)
    #             self.get_windows_img()  # take screenshot
    #     elif selector_by == "n" or selector_by == 'name':
    #         element = self.driver.find_element_by_name(selector_value)
    #     elif selector_by == "c" or selector_by == 'class_name':
    #         element = self.driver.find_element_by_class_name(selector_value)
    #     elif selector_by == "l" or selector_by == 'link_text':
    #         element = self.driver.find_element_by_link_text(selector_value)
    #     elif selector_by == "p" or selector_by == 'partial_link_text':
    #         element = self.driver.find_element_by_partial_link_text(selector_value)
    #     elif selector_by == "t" or selector_by == 'tag_name':
    #         element = self.driver.find_element_by_tag_name(selector_value)
    #     elif selector_by == "x" or selector_by == 'xpath':
    #         try:
    #             element = self.driver.find_element_by_xpath(selector_value)
    #             logger.info("Had find the element \' %s \' successful "
    #                         "by %s via value: %s " % (element.text, selector_by, selector_value))
    #         except NoSuchElementException as e:
    #             logger.error("NoSuchElementException: %s" % e)
    #             self.get_windows_img()
    #     elif selector_by == "s" or selector_by == 'selector_selector':
    #         element = self.driver.find_element_by_css_selector(selector_value)
    #     else:
    #         raise NameError("Please enter a valid type of targeting elements.")
    #
    #     return element
    #
    #
    # 输入
    def type(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info('Had type \' %s \' in inputBox' % text)
        except NameError as e:
            logger.info('Failed type into input box with %s' % text)
            self.get_windows_img()

    # 清除文本框
    def clear(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info('clear text in input box before typing.')
        except NameError as e:
            logger.info('Failed to clear text in input box with %s' % e)
            self.get_windows_img()


    # 点击元素
    def click(self, selector):
        el = self.find_element(selector)
        try:
            logger.info('the element / %s / is clicked.' % el.text)
            el.click()

        except NameError as e:
            logger.info('Failed to click the element with %s' % e)
            self.get_windows_img()


