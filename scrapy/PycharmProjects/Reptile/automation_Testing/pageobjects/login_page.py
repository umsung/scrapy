from framework.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# 登陆

class LoginPage(BasePage):
    # 四、selenium常见异常
    # 1.
    # NoSuchElementException：没有找到元素
    # 2.
    # NoSuchFrameException：没有找到iframe
    # 3.
    # NoSuchWindowException: 没找到窗口句柄handle
    # 4.
    # NoSuchAttributeException: 属性错误
    # 5.
    # NoAlertPresentException：没找到alert弹出框
    # 6.
    # ElmentNotVisibleException：元素不可见
    # 7.
    # ElementNotSelectableException：元素没有被选中
    # 8.
    # TimeoutException：查找元素超时

    # input_loc = ("id", "kw")
    login_btn = (By.XPATH, '//*[@id="currentAccount_Div"]/a[1]')
    username_input = (By.XPATH, '//*[@id="UserName"]')
    password_input = (By.XPATH, "//*[@id='PassWord']")
    signin_btn = (By.XPATH, "//*[@id='loginSubmit']")

    def click_login_btn(self):
        self.expected_conditions(self.login_btn).click()

    def login(self, username, password):
        self.expected_conditions(self.username_input).send_keys(username)
        self.find_element(*self.password_input).send_keys(password)
        self.find_element(*self.signin_btn).click()

