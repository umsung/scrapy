from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from pymongo import MongoClient

class sliderVeCode(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 5)
        # self.client = MongoClient('127.0.0.1')
        # self.db = self.client['db_name']
        # self.collection = self.db['table_name']
    
    def get_track(self,distance):
        # 定义滑动轨迹，先快后慢
        track = []
        current = 0
        mid = distance * 3 / 4
        t = 0.2
        v = 0
        while current < distance:
            if current < mid:
                a = 2
            else:
                a = -3
            v0 = v
            v = v0 + a * t
            move = v0 * t + 1 / 2 * a * t * t
            current += move
            track.append(round(move))
        return track

    def login(self):
        self.driver.get('https://www.qichacha.com/user_login?back=%2Fsearch%3Fkey%3D%25E6%2588%2590%25E5%259D%2587%25EF%25BC%2588%25E4%25B8%258A%25E6%25B5%25B7%25EF%25BC%2589%25E6%2595%2599%25E8%2582%25B2%25E5%259F%25B9%25E8%25AE%25AD%25E6%259C%2589%25E9%2599%2590%25E5%2585%25AC%25E5%258F%25B8')
        time.sleep(1)
        # perform()用来执行ActionChains中存储的行为
        self.driver.find_element_by_xpath('//*[@id="verifyLogin"]').click()
        sliderButton = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="nc_1_n1z"]')))
        ActionChains(self.driver).click_and_hold(sliderButton).perform()
        track = self.get_track(330)
        for i in track:
            print(i)
            ActionChains(self.driver).move_by_offset(i,0).perform()
            ActionChains(self.driver).reset_actions()
        ActionChains(self.driver).release().perform()

if __name__ == "__main__":
    s = sliderVeCode()
    s.login()