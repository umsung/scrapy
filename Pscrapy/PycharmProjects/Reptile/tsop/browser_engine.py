from selenium import webdriver


class BrowserEngine(object):
    """
        定义一个浏览器引擎类，根据browser_type的值去，控制启动不同的浏览器，这里主要是IE，Firefox, Chrome
    """

    def __init__(self, driver):

        self.driver = driver

    browser_type = 'Chrome'

    def get_browser(self):
        if self.browser_type == 'Chrome':
            driver = webdriver.Chrome()
        elif self.browser_type == 'Firefox':
            driver = webdriver.Firefox()
        elif self.browser_type == 'IE':
            driver = webdriver.Ie
        else:
            driver = webdriver.Chrome()

        driver.maximize_window()
        driver.implicitly_wait(10)

        return driver
