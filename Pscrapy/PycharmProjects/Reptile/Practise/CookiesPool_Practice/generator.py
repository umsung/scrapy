from db import *
from selenium import webdriver
from config import *
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CookiesGenerator(object):
    def __init__(self,name, browser_type = BROWSER_TYPE):
        self.name = name
        self.cookies_db = CookiesRedisClient(name = self.name)
        self.account_db = AccountRedisClient(name = self.name)
        self.browser_type = browser_type

    def _init_browser(self,browser_type):
        if browser_type == '':
            caps = DesiredCapabilities.PHANTOMJS
            caps[
                "phantomjs.page.settings.userAgent"] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
            self.browser = webdriver.PhantomJS(desired_capabilities=caps)
            self.browser.set_window_size(1400, 500)
        if browser_type == 'Chrome':
            self.browser = webdriver.Chrome()
            self.wait = WebDriverWait(self.browser,5)

    def set_cookies(self, account, password):
        cookie = self.new_cookies(account,password)
        self.cookies_db.set(account,cookie)

    def new_cookies(self, account, password):
        raise NotImplementedError

    def run(self):
        cookies = self.cookies_db.all()  # [{username:'',password:''},{username:'',password:''}]
        accounts = self.account_db.all()
        cookies_name = [cookie['username'] for cookie in cookies]
        if len(accounts):
            self._init_browser(self.browser_type)
        for account in accounts:
            if account['username'] not in cookies_name:
                print('创建')
                self.set_cookies(account['username'] ,account['password'] )
        print('Generator Run Finished')
    
    def close(self):
        try:
            self.browser.close()
            del self.browser
            print('close browser')
        except TypeError:
            print('not close browser')


class WeiboCookiesGenerator(CookiesGenerator):
    def __init__(self,name='', browser_type = ''):

        CookiesGenerator.__init__(self,name,browser_type)
        self.name = name
    
    def new_cookies(self,account, password):
        self.browser.get('')
        try:
            username_position = self.wait.until(EC.presence_of_element_located((By.XPATH, '')))
            password_position = self.wait.until(EC.presence_of_element_located((By.XPATH, '')))
            submit = self.wait.until(EC.presence_of_element_located((By.XPATH, '')))
            username_position.send_keys(account)
            password_position.send_keys(password)
            submit.click()
            title = self.wait.until(EC.presence_of_element_located((By.XPATH, '')))
            item = {}
            if '' in title:
                cookies = self.browser.get_cookies()
                for cookie in cookies:
                    item[cookie['name']] = cookies['value']
        except TimeoutError:
            print('出现验证码')
  