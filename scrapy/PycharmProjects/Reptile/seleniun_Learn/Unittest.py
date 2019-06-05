import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def fun(x):
    return x+1


class MyTest(unittest.TestCase):
    '''
    根据用例名称执行

    '''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def testcc(self):
        self.assertEqual(fun(3), 4)

    def testAdd(self):
        self.assertEqual((1+2), 3)
        self.assertEqual((1+2), 3)

    def testMultiply(self):
        self.assertEqual((0*10), 0)
        self.assertEqual((5*8), 40)

    def testMInus(self):
        result = 6-5
        hope = 1
        self.assertEqual(result, hope)

    def testDivide(self):
        result = 6/2
        hope = 3.5
        self.assertEqual(result, hope, msg='失败原因: %s != %s' % (result, hope))

    @unittest.skip()
    def login(self, username, psd):
        self.driver.find_element_by_id('//*[@id="UserName"]').send_keys(username)
        self.driver.find_element_by_id('//*[@id="PassWord"]').send_keys(psd)
        self.driver.find_element_by_id('//*[@id="loginSubmit"]').click()

    @unittest.skip()
    def is_login_success(self):
        try:
            name = self.driver.find_element(By.XPATH, '').text
            print(name)
            return True
        except Exception:
            return False

    @unittest.skip()
    def test_title01(self):
        print('执行测试用例1')
        try:
            assert '标题' in self.driver.title
            print('Pass')
        except Exception:
            print('Fail')

    @unittest.skip()
    def test_login01(self):
        print('执行登陆测试用例1')
        self.login('19900000000', '123456')
        result = self.is_login_success()
        self.assertTrue(result)

    @unittest.skip(u'无条件跳过次用例')
    def test_login02(self):
        print('执行登陆测试用例2')
        self.login('19900000001', '123456')
        result = self.is_login_success()
        self.assertTrue(result)

    def test_01(self):
        u'''验证元素存在：博客园'''
        locator = ("id", "blog_nav_sitehome")
        text = u"博客园"
        result = EC.text_to_be_present_in_element(locator, text)(self.driver)
        self.assertTrue(result)

    def test_02(self):
        u'''验证元素存在：首页'''
        locator = ("id", "blog_nav_myhome")
        text = u"首页"
        result = EC.text_to_be_present_in_element(locator, text)(self.driver)
        self.assertTrue(result)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()