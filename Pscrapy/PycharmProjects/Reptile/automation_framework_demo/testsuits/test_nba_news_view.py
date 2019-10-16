import unittest
from automation_framework_demo.framework.browser_engine import *
from automation_framework_demo.pageobjects.baidu_homepage import *
from automation_framework_demo.pageobjects.baidu_news_home import *
from automation_framework_demo.pageobjects.news_sport_home import *
from selenium.webdriver.common.by import By

class ViweNBANews(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_view_nba_views(self):
        homepage = HomePage(self.driver)
        homepage.click_news_btn()
        # self.driver.find_element_by_xpath('//*[@id="u1"]/a[@name="tj_trnews"]').click()

        newshome = NewsHomePage(self.driver)
        newshome.click_sports_link()
        # self.driver.find_element_by_xpath('//*[@id="channel-all"]/div/ul/li[5]/a').click()
        # newshome.find_element(By.XPATH, '//*[@id="channel-all"]/div/ul/li[5]/a').click()

        sportnewhome = SportNewsHomePage(self.driver)
        sportnewhome.click_nba_link()
        # self.driver.find_element_by_xpath('//*[@id="channel-all"]/div/ul/li[6]/a[1]').click()

        # sportnewhome.get_windows_img()


if __name__ == '__main__':
    unittest.main()