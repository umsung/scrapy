from framework.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.logger import Logger
import time
import random
# 现货

logger = Logger('GoodsPrompt').getlog()


class GoodsPrompt(BasePage):
    thlink = (By.XPATH, "//*[@class='thlink']")
    navbox = (By.XPATH, "//*[@class='navbox']/a[2]")
    gopage = (By.XPATH, '//*[@id="gopage"]')
    AddCart_list = (By.CLASS_NAME, 'addbtn')
    goods_click_random = (By.XPATH, "//*[@class='box']/div/span//dl/dt/a[1]")
    pay_btn = (By.XPATH, '//*[@id="Pay"]')
    AddCart_detail = (By.XPATH, "//*[@id='AddCart']")
    store = (By.XPATH, "//*[@id='store']")
    priceS = (By.XPATH, '//*[@class="price-v"] | //*[@class="fleft"]/span[1]')

    uniprice = (By.XPATH, '//*[@class="uniprice "]/span')
    num = (By.XPATH, '//*[@class="order-amount"]')
    spanPay = (By.XPATH, '//*[@id="spanPay"]')

    btnToPay = (By.XPATH, "//*[@id='btnToPay']")

    transport_check = (By.XPATH, '//*[@class="transport-check"]/label/input')
    btn_payment = (By.XPATH, "//*[@class='btn-payment']")

    pay_zfb = (By.XPATH, "//*[@class='pay-zfb']")
    pay_cft = (By.XPATH, "//*[@class='pay-cft']")

    def navbox_buy(self):
        try:
            self.expected_conditions(self.thlink).click()
            self.expected_conditions(self.gopage)
            self.expected_conditions(self.navbox).click()
            self.expected_conditions(self.gopage)
            self.find_elements(*self.AddCart_list)[random.randint(0, 40)].click()
            self.find_elements(*self.goods_click_random)[random.randint(0, 49)].click()
            self.switch_to(1)

            self.expected_conditions(self.AddCart_detail).click()
            self.expected_conditions(self.store).click()
            time.sleep(3)
            price = self.expected_conditions(self.priceS).text
            price = price.replace('¥', '')
            print(price)
            self.expected_conditions(self.pay_btn).click()

            z_price = self.expected_conditions(self.uniprice).text
            z_price = z_price.replace('¥', '')
            print(z_price)

            order_amount = self.expected_conditions(self.num).text
            t_price = self.expected_conditions(self.spanPay).text
            t_price = t_price.replace(',', '')
            print(t_price)

            if float(price) * 0.9 == float(z_price) or float(price) == float(z_price):
                if float(z_price) * int(order_amount) == float(t_price):
                    logger.info('现货价格正确:{}'.format(t_price))
                    self.find_element(*self.btnToPay).click()
                else:
                    logger.info('现货总价错误:{}'.format(t_price))
                    self.get_windows_img()
                    self.expected_conditions(self.btnToPay).click()
            else:
                logger.info('现货折后单价错误:{}'.format(z_price))
                self.get_windows_img()
                self.expected_conditions(self.btnToPay).click()

            # self.expected_conditions(self.btn_payment).click()

            # 如果存在配送方式。则随机选择
            if self.isElementExist(*self.transport_check):
                self.find_elements(*self.transport_check)[random.randint(0, 1)].click()

            # 默认方式微信支付
            self.find_element(*self.btn_payment).click()
            time.sleep(1)
            logger.info('微信支付')
            self.back()

            # 支付宝支付
            self.expected_conditions(self.pay_zfb).click()
            self.find_element(*self.btn_payment).click()
            time.sleep(1)
            logger.info('支付宝支付')
            self.back()

            # 财付通支付
            self.expected_conditions(self.pay_cft).click()
            self.find_element(*self.btn_payment).click()
            time.sleep(1)
            logger.info('财付通支付')
            self.close()
            self.switch_to(0)

            # 随机点击现货酒款-法国
            self.move_to(*self.navbox)
            time.sleep(0.5)
            self.find_elements(By.XPATH, "//*[@class='extend-xl']/dl//a")[random.randint(0, 9)].click()
            self.switch_to(1)
            self.expected_conditions(self.gopage)
            self.close()
            self.switch_to(0)

            # 随机点击现货酒款-意大利
            self.move_to(*self.navbox)
            time.sleep(0.5)
            self.find_elements(By.XPATH, "//*[@class='extend-xl']/div[1]//a")[random.randint(0, 6)].click()
            self.switch_to(1)
            self.expected_conditions(self.gopage)
            self.close()
            self.switch_to(0)

            # 随机点击现货酒款-西班牙以下
            self.move_to(*self.navbox)
            time.sleep(0.5)
            self.find_elements(By.XPATH, "//*[@class='extend-xl']/div[2]//a")[random.randint(0, 5)].click()
            self.switch_to(1)
            self.expected_conditions(self.gopage)
            self.close()
            self.switch_to(0)
        except Exception:
            logger.info('navbox_buy error')
            self.get_windows_img()
