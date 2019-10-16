from framework.base_page import BasePage
import time
from selenium.webdriver.common.by import By
import random
from framework.logger import *

logger = Logger('Primeur').getlog()


class Primeur(BasePage):
    navbox = (By.XPATH, "//*[@class='navbox']/a[4]")
    gopage = (By.XPATH, '//*[@id="gopage"]')
    qj_sort = (By.XPATH, "//*[@class='qj-sort']/ul/li[9]")

    addExpectcart = (By.CLASS_NAME, "addExpectcart")
    lazy = (By.CLASS_NAME, "lazy")
    pay_btn = (By.XPATH, '//*[@id="Pay"]')

    addcart_detail = (By.XPATH, "//*[@id='AddCart']")

    priceS = (By.XPATH, '//*[@class="price-v"]')

    ReceiveEmail = (By.XPATH, "//*[@id='ReceiveEmail']")
    checkexpect = (By.XPATH, "//*[@id='checkexpect']")
    num = (By.XPATH, '//*[@class="order-amount"]')
    spanPay = (By.XPATH, '//*[@id="spanPay"]')

    btnToPay = (By.XPATH, "//*[@id='btnToPay']")

    btn_payment = (By.XPATH, "//*[@class='btn-payment']")
    pay_zfb = (By.XPATH, "//*[@class='pay-zfb']")
    pay_cft = (By.XPATH, "//*[@class='pay-cft']")

    pri_input = (By.XPATH, "//*[@class='st-out']/input[1]")
    pri_submit = (By.XPATH, "//*[@class='st-out']/input[2]")


    def primeur_buy(self, email):
        self.find_element(*self.navbox).click()
        self.expected_conditions(self.gopage)

        self.find_element(*self.qj_sort).click()
        time.sleep(1.5)
        self.find_element(*self.qj_sort).click()
        time.sleep(1.5)

        self.find_elements(*self.addExpectcart)[random.randint(0, 49)].click()
        time.sleep(1)
        self.find_elements(*self.lazy)[random.randint(0, 49)].click()

        self.switch_to(1)

        self.expected_conditions(self.addcart_detail).click()

        price = self.expected_conditions(self.priceS).text
        price = price.replace('¥', '')

        self.expected_conditions(self.pay_btn).click()
        self.expected_conditions(self.ReceiveEmail).clear()
        time.sleep(0.5)
        self.find_element(*self.ReceiveEmail).send_keys(email)
        self.expected_conditions(self.checkexpect).click()

        order_amount = self.expected_conditions(self.num).text
        t_price = self.expected_conditions(self.spanPay).text
        t_price = t_price.replace(',', '')

        if float(price) * int(order_amount) == float(t_price):
            logger.info('期酒价格正确:{}'.format(price))
        else:
            logger.info('期酒价格错误:{}'.format(price))
            self.get_windows_img()

        self.expected_conditions(self.btnToPay).click()
        time.sleep(1)

        # 默认微信支付方式
        self.expected_conditions(self.btn_payment).click()
        time.sleep(1)
        self.back()

        # 支付宝支付
        self.expected_conditions(self.pay_zfb).click()
        self.expected_conditions(self.btn_payment).click()
        time.sleep(1)
        self.back()

        # 财付通支付
        self.expected_conditions(self.pay_cft).click()
        self.expected_conditions(self.btn_payment).click()
        time.sleep(1)
        self.close()

        self.switch_to(0)

    def primeur_search(self, text):
        self.expected_conditions(self.pri_input).send_keys(text)
        self.expected_conditions(self.pri_submit).click()

        self.move_to(*self.navbox)

        self.find_elements(By.XPATH, "//*[@class='extend-qj']/dl//a")[random.randint(0, 7)].click()

        self.expected_conditions((By.XPATH, "//*[@class='qj-sort']/ul/li[9]")).click()