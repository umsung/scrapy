from autoTest.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage(BasePage):
    """页面模块 登陆页面"""
    username = (By.ID, 'username')
    password = (By.ID, 'password')
    dialogTitle = (By.XPATH, "//h3[@class=\"modal-title ng-binding\"]")
    cancelButton = (By.XPATH, '//button[@class=\"btn btn-warning ng-binding\"][@ng-click=\"cancel()\"]')
    okButton = (By.XPATH, '//button[@class=\"btn btn-primary ng-binding\"][@ng-click=\"ok()\"]')

    def set_username(self, username):
        self.driver.find_element(*LoginPage.username).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*LoginPage.password).send_keys(password)

    def get_DiaglogTitle(self):
        return self.driver.find_element(*LoginPage.dialogTitle).text

    def get_CanceButton(self):
        return self.driver.find_element(*LoginPage.cancelButton).click()

    # Get "cancel" button and then click
    def click_cancel(self):
        cancelbtn = self.driver.find_element(*LoginPage.cancelButton)
        cancelbtn.click()

        # click Sign in

    def click_SignIn(self):
        okbtn = self.driver.find_element(*LoginPage.okButton)
        okbtn.click()