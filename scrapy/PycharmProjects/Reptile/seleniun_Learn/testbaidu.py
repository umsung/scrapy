import unittest
from selenium import webdriver
import time, os
from tsop.browser_engine import *


class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.driver = BrowserEngine(self).get_browser()

        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(10)
        self.driver.get('https://www.baidu.com')

    def tearDown(self):
        self.driver.quit()

    def test_baidu_search(self):
        self.driver.find_element_by_id('kw').send_keys('seenum')
        time.sleep(1)
        try:
            assert 'selenium' in self.driver.title
            print('pass')
        except Exception as e:
            print('error.', format(e))

    def test_back(self):
        self.driver.find_element_by_id('kw').send_keys(u'端')
        time.sleep(1)
        self.driver.back()


if __name__ == '__main__':
    unittest.main()