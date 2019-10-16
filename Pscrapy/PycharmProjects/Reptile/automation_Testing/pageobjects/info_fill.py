from framework.base_page import BasePage
from selenium.webdriver.common.by import By
import time

# 信息编辑

class InfoFill(BasePage):
    mygoods_btn = (By.XPATH, '//*[@id="currentAccount_Div"]/a[2]')
    account_btn = (By.XPATH, '//*[@id="u-m-list"]/li[11]/a')
    address_btn = (By.XPATH, '//*[@class="u-t-tm"]/a[contains(./text(),"收货地址")]')
    new_address_btn = (By.XPATH, '//*[@class="new-address"]')
    txtname = (By.XPATH, '//*[@id="txtname"]')
    provices = (By.XPATH, '//*[@id="provices"]/option[3]')
    citys = (By.XPATH, '//*[@id="citys"]/option[3]')
    areas = (By.XPATH, '//*[@id="areas"]/option[3]')
    txtstreetaddress = (By.XPATH, '//*[@id="txtstreetaddress"]')
    txtmobile = (By.XPATH, '//*[@id="txtmobile"]')
    yesbtn = (By.XPATH, '//*[@class="yesbtn"]')

    # 信息编辑
    def message_edit(self, txtname, txtstreetaddress, txtmobile):
        self.expected_conditions(self.mygoods_btn).click()
        self.expected_conditions(self.account_btn).click()
        self.expected_conditions(self.address_btn).click()
        self.expected_conditions(self.new_address_btn).click()
        self.expected_conditions(self.txtname).send_keys(txtname)
        time.sleep(0.5)
        self.find_element(*self.provices).click()
        time.sleep(0.5)
        self.find_element(*self.citys).click()
        time.sleep(0.5)
        self.find_element(*self.areas).click()
        time.sleep(0.5)
        self.expected_conditions(self.txtstreetaddress).send_keys(txtstreetaddress)
        self.expected_conditions(self.txtmobile).send_keys(txtmobile)
        self.expected_conditions(self.yesbtn).click()


