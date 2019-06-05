from selenium.webdriver.common.by import By

from automation_framework_demo.framework.base_page import BasePage


class SportNewsHomePage(BasePage):
    # nba_link = 'xpath=>//*[@id="channel-submenu"]/div/span[2]/a[1]'
    nba_link = (By.XPATH, '//*[@id="integrated-aside-video"]/div[1]/h3/a')

    def click_nba_link(self):
        self.find_element(*self.nba_link).click()
        h = self.current_window()
        # self.get_windows_img()
        self.switch_to(1)
        self.close()
        self.switch_to(0)
        self.find_element(*self.nba_link).click()

        # self.switch_to_window(partial_url='', partial_title='')
        # self.sleep(2)
        # self.switch_to_window(partial_url='', partial_title='')



        # self.click(self.nba_link)
