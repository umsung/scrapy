from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tsop.basepage import BasePage
from tsop.browser_engine import BrowserEngine


class BaiduSearch(object):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    h = driver.current_window_handle
    wait = WebDriverWait(driver, 10)
    basepage = BasePage(driver)

    def open_baidu(self):
        self.basepage.open_url('https://www.baidu.com')
        time.sleep(1)

    def test_search(self):
        # self.driver.find_element_by_id('kw').send_keys('selenium')
        inp = self.wait.until(EC.presence_of_element_located((By.ID, 'kw')))
        submit = self.wait.until(EC.presence_of_element_located((By.ID, 'su')))
        inp.send_keys('selenium')
        time.sleep(1)
        print(self.driver.title)
        try:
            assert 'selenium' in self.driver.title
            print('test pass')
        except TimeoutError:
            return self.test_search()
        except Exception as e:
            print('fail')
        self.basepage.back()
        self.basepage.forward()
        self.basepage.take_screenshot()

        self.basepage.quit_browser()


baidu = BaiduSearch()
baidu.open_baidu()
baidu.test_search()