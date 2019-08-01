import time
import unittest
from framework.browser_engine import *
from framework.logger import *
from pageobjects.baidu_homepage import *

logger = Logger('BaiduSearch').getlog()


class BaiduSearch(unittest.TestCase):
    """
        集成Unittest.testcase
    """
    @classmethod
    def setUpClass(cls):
        """
             测试固件的setUp()的代码，主要是测试的前提准备工作
             :return:
         """
        cls.browser = BrowserEngine(cls)
        cls.driver = cls.browser.open_browser()
        # cls.driver = webdriver.Chrome()
        # cls.driver.get('www.baidu.com')


    @classmethod
    def tearDownClass(cls):
        cls.browser.browser_quit()


        """
               测试结束后的操作，这里基本上都是关闭浏览器
               :return:
        """
        # logger.info('quit')


    def test_baidu_search(self):
        self.driver.find_element_by_id('kw').send_keys('ces')
        # homepage = HomePage(self.driver)
        # homepage.type_search('selenium')
        # homepage.click_submit_btn()
        # time.sleep(1)
        #
        # try:
        #     assert 'selenium' in self.driver.title
        #     print('pass')
        # except NameError as e:
        #     print('error', format(e))
        #     homepage.get_windows_img()


        # self.driver.find_element_by_id('kw').send_keys('selenium')
        # time.sleep(2)
        # try:
        #     assert 'selenium' in self.driver.title
        #     print('pass')
        # except Exception as e:
        #     print('error', format(e))

    def test_search2(self):
        self.driver.find_element_by_id('kw').send_keys('123')
        # homepage = HomePage(self.driver)
        # homepage.type_search('python')
        # homepage.click_submit_btn()
        # time.sleep(2)
        # homepage.get_windows_img()


if __name__ == '__main__':
    unittest.main()