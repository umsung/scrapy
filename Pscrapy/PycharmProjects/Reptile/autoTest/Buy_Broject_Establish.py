from selenium import webdriver
import unittest#第一步引入一个unittest
import time


class Buy_Broject_Establish(unittest.TestCase):#第二步创建继承一个unittest.TestCase的类
    def setUp(self):#第三步定义一个setup，放一些准备的工作，或者准备一些测试数据。
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()#放大浏览器
        self.driver.get("http://10.20.24.45:8080/amcs/login.htm")
        print(self.driver.title)#获取标题头并打印出来
        print(self.driver.current_url)#获取当前页面的url
        time.sleep(5)
    def test_001(self):#进入登录页面
        self.driver.find_element_by_id('account_content').send_keys("admin")#输入账号
        self.driver.find_element_by_id('account_pass').send_keys("1")#输入密码
        self.driver.find_element_by_id('submitBtn').click()#点击登录
        time.sleep(2)
        print(u'进入首页')
    def test_002(self):#进入收购项目管理首页
        self.driver.find_element_by_xpath('//*[@id="J-h-menu-body"]/ul/li[3]/a').click()#进入项目管理
        self.driver.find_element_by_xpath('//*[@id="J-h-menu-body"]/ul/li[3]/ul/li[1]/a/span').click()#进入收购项目管理
        self.driver.implicitly_wait(5)#隐试等待
        self.driver.switch_to.frame('mainFrame_assetPacketManagePro')#进入一个iframe。
        time.sleep(10)
        print('进入收购项目管理')
    def tearDown(self):#第三步：定义一个tearDown，当我在测试完的时候我要对测试有一个销毁的过程比如说关闭浏览器，那么我们就写在tearDown当中
            self.driver.quit()
if __name__ == '__main__':#如果其他的类调用的这个类的时候他就会自动忽略掉这个函数，他是为了测试自身的类用的
    unittest.main()#启动程序