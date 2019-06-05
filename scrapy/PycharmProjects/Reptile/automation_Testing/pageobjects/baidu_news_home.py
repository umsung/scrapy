from automation_framework_demo.framework.base_page import *
from selenium.webdriver.common.by import By

class NewsHomePage(BasePage):
    # sports_link = 'xpath=>//*[@id="channel-all"]/div/ul/li[5]/a'
    sports_link = (By.XPATH, '//*[@id="channel-all"]/div/ul/li[7]/a')

    def click_sports_link(self):
        self.find_element(*self.sports_link).click()

        # self.click(self.sports_link)
