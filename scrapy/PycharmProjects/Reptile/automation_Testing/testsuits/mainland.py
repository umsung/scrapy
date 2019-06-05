import unittest
from framework.browser_engine import BrowserEngine
from framework.logger import Logger
from pageobjects.login_page import LoginPage
from pageobjects.info_fill import InfoFill
from pageobjects.search_filter import SearchFilter
from pageobjects.prompt_goods import GoodsPrompt
from pageobjects.primeur import Primeur

logger = Logger('MainLand').getlog()
username = 19900000314
password = 123456

class MainLand(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_mainland_login(self):
        # 登陆
        loginpage = LoginPage(self.driver)
        loginpage.click_login_btn()
        loginpage.login(username, password)
        logger.info('登陆成功')

        # 信息编辑
        infofill = InfoFill(self.driver)
        infofill.message_edit('测试', '测试', username)

        # 搜索筛选
        searchfilter = SearchFilter(self.driver)
        searchfilter.search('葡萄酒')
        searchfilter.filter()

        # 现货购买流程
        goodsprompt = GoodsPrompt(self.driver)
        goodsprompt.navbox_buy()

        # 期酒购买流程
        primeur = Primeur(self.driver)
        primeur.primeur_buy('123@qq.com')
        primeur.primeur_search('葡萄')


if __name__ == '__main__':
    unittest.main()