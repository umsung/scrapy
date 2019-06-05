from framework.base_page import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class HomePage(BasePage):
    # input_box = 'id=>kw'
    # search_submit_btn = 'xpath=>//*[@id="su"]'
    # news_btn = 'xpath=>//*[@id="u1"]/a[@name="tj_trnews"]'
    input_box = (By.ID, 'kw')
    search_submit_btn = (By.XPATH, '//*[@id="su"]')
    news_btn = (By.XPATH, '//*[@id="u1"]/a[@name="tj_trnews"]')

    def type_search(self, text):
        self.type(self.input_box, text)
        self.find_element(self.input_box).send_keys(text)

    def click_submit_btn(self):
        self.click(self.search_submit_btn)

    def click_news_btn(self):
        # self.click(self.news_btn)
        self.find_element(*self.news_btn).click()
