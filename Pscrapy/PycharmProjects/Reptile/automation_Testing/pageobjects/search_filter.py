from framework.base_page import BasePage
from selenium.webdriver.common.by import By
import random
import time
from framework.logger import Logger
# 搜索筛选
logger = Logger('SearchFilter').getlog()

class SearchFilter(BasePage):
    input = (By.ID, 'q')
    btn = (By.CLASS_NAME, 'buts')
    random_click = (By.XPATH, '//*[@class="box"]/div/span//dl/dt/a[1]')
    pay_btn = (By.XPATH, '//*[@id="Pay"]')
    series_retrieval = (By.XPATH, '//*[@class="retrieval"]/dl[3]/dd/a')
    proc_retrieval = (By.XPATH, '//*[@class="retrieval"]/dl[2]/dd/a')
    reset = (By.XPATH, '//*[@class="reset-xj"]')

    def search(self, input):
        try:
            self.expected_conditions(self.input).send_keys(input)
            self.expected_conditions(self.btn).click()
            logger.info('输入框输入{}，点击搜索'.format(input))
        except TypeError as e:
            logger.info('search error', format(e))
            self.get_windows_img()

    def filter(self):
        try:
            self.find_elements(*self.random_click)[random.randint(0, 49)].click()
            logger.info('随机点击搜索酒款')

            self.switch_to(1)
            self.expected_conditions(self.pay_btn)
            self.driver.close()
            self.switch_to(0)
            time.sleep(0.5)

            self.find_elements(*self.series_retrieval)[random.randint(1,3)].click()
            time.sleep(0.5)
            logger.info('系列筛选')

            self.find_elements(*self.proc_retrieval)[random.randint(1,7)].click()
            time.sleep(0.5)
            logger.info('产区筛选')

            self.expected_conditions(self.reset).click()
            logger.info('清空筛选')
        except Exception:
            logger.info('filter error')
            self.get_windows_img()