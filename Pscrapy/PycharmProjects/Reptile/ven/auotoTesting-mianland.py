# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 16:48:35 2018

@author: Administrator
"""

from selenium import webdriver
import random
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
    

driver=webdriver.Chrome()
wait = WebDriverWait(driver,10)
driver.get("http://mall.wine-world.com/")
h=driver.current_window_handle
driver.maximize_window()
driver.implicitly_wait(15)

#登陆
signInBut = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="currentAccount_Div"]/a[1]')))
signInBut.click()
#driver.find_element_by_xpath("//*[@class='box']/div[2]/a[1]").click()
driver.find_element_by_xpath("//*[@id='UserName']").send_keys("19900000199")
time.sleep(0.1)
driver.find_element_by_xpath("//*[@id='PassWord']").send_keys("123456")
time.sleep(0.1)
driver.find_element_by_xpath("//*[@id='loginSubmit']").click()



#排序筛选下一页
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='buts']"))).click()
# =============================================================================
# driver.find_element_by_class_name("buts").click()
# =============================================================================
#time.sleep(1)
driver.find_element_by_id("q").send_keys(u"葡萄酒")
#time.sleep(1)
driver.find_element_by_class_name("buts").click()
#time.sleep(2)

#随机点击一款酒
driver.find_elements_by_xpath("//*[@class='box']/div/span//dl/dt/a[1]")[random.randint(0,49)].click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="Pay"]')))
driver.close()
driver.switch_to.window(h)
time.sleep(0.5)


#产区筛选
s=driver.find_elements_by_xpath("//*[@class='retrieval']/dl[2]/dd/a")
s[random.randint(1, 7)].click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@class='retrieval']/dl[2]/dd/a[1]").click()
time.sleep(0.5)


#类型筛选
s=driver.find_elements_by_xpath("//*[@class='retrieval']/dl[3]/dd/a")
s[random.randint(1, 3)].click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@class='retrieval']/dl[3]/dd/a[1]").click()
time.sleep(0.5)


#品种筛选
s=driver.find_elements_by_xpath("//*[@class='retrieval']/dl[4]/dd/div/a")
s[random.randint(1, 13)].click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@class='retrieval']/dl[4]/dd/div/a[1]").click()
time.sleep(0.5)

#价格筛选
s=driver.find_elements_by_xpath("//*[@class='retrieval']/dl[5]/dd/a")
s[random.randint(1, 5)].click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@class='retrieval']/dl[5]/dd/a[1]").click()
time.sleep(0.5)

#系列筛选
s=driver.find_elements_by_xpath("//*[@class='retrieval']/dl[6]/dd/div/a")
s[random.randint(1, 21)].click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@class='retrieval']/dl[6]/dd/div/a[1]").click()
time.sleep(0.5)

#评分筛选
s=driver.find_elements_by_xpath("//*[@class='retrieval']/dl[7]/dd/a")
s[random.randint(1,3)].click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@class='retrieval']/dl[7]/dd/a[1]").click()
time.sleep(0.5)

#清空筛选
driver.find_element_by_xpath("//*[@class='reset-xj']").click()
time.sleep(0.5)

#排序
driver.find_element_by_xpath("//*[@class='paixu']/ul/li[2]/a").click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@class='paixu']/ul/li[2]/a").click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@class='paixu']/ul/li[3]/a").click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@class='paixu']/ul/li[3]/a").click()
time.sleep(0.5)

#翻页
driver.find_element_by_xpath("//*[@class='w-page']/ul/li[1]/a").click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@class='w-page']/ul/li[1]/a").click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@class='w-page']/ul/li[2]/a").click()
time.sleep(0.5)

#点击跨境电商
driver.find_element_by_xpath("//*[@class='retrieval']/dl[1]/dd[2]/a").click()
time.sleep(0.2)

#点击期酒
driver.find_element_by_xpath("//*[@class='retrieval']/dl[1]/dd[3]/a").click()
time.sleep(0.2)

######以上是搜索功能点击


#点击选购中心
driver.find_element_by_xpath("//*[@class='thlink']").click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))


#点击现货酒款
driver.find_element_by_xpath("//*[@class='navbox']/a[2]").click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@class="s-ext"]')))


#点击展开更多
driver.find_element_by_xpath("//*[@class='s-ext']").click()



#购买现货酒款
#随机点击一个名庄
driver.find_elements_by_xpath("//*[@id='showProductList']//dl/dt/a[2]")[random.randint(0,20)].click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))
driver.back()
time.sleep(0.3)

#点击+号  将第一个商品加入购物车
driver.find_element_by_xpath("//*[@id='showProductList']/dl[1]/dd/div/div/p/a[2]").click()
time.sleep(0.2)

driver.find_element_by_xpath("//*[@id='showProductList']/dl[1]/dd/div/span").click()
time.sleep(0.2)


#随机选择一个商品加入购物车
driver.find_elements_by_class_name("addbtn")[random.randint(0,40)].click()
time.sleep(0.3)

#随机点击一个商品
driver.find_elements_by_xpath("//*[@class='box']/div/span//dl/dt/a[1]")[random.randint(0,49)].click()
time.sleep(1)
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="Pay"]')))


#点击商品详情+号
driver.find_element_by_xpath("//*[@class='buy-func']/span[1]").click()
time.sleep(0.5)
#点击商品详情-号
driver.find_element_by_xpath("//*[@class='buy-func']/span[2]").click()
time.sleep(0.5)


#点击加入购物车
driver.find_element_by_xpath("//*[@id='AddCart']").click()
time.sleep(0.5)

#点击收藏
driver.find_element_by_xpath("//*[@id='store']").click()
time.sleep(3)

#点击立即购买
driver.find_element_by_xpath("//*[@id='Pay']").click()
time.sleep(1.5)


#点击提交订单
driver.find_element_by_xpath("//*[@id='btnToPay']").click()
time.sleep(1.5)



#随机选择配送方式
driver.find_elements_by_xpath("//*[@class='transport-check']/label/input")[random.randint(0,1)].click()
time.sleep(1)

#点击支付
driver.find_element_by_xpath("//*[@class='btn-payment']").click()
time.sleep(1.5)
driver.back()


#选择支付宝支付方式
driver.find_element_by_xpath("//*[@class='pay-zfb']").click()
time.sleep(1)

#随机选择配送方式
driver.find_elements_by_xpath("//*[@class='transport-check']/label/input")[random.randint(0,1)].click()
time.sleep(1)

#点击支付
driver.find_element_by_xpath("//*[@class='btn-payment']").click()
time.sleep(1)
driver.back()


#选择财付通支付方式
driver.find_element_by_xpath("//*[@class='pay-cft']").click()
time.sleep(1)

#随机选择配送方式
driver.find_elements_by_xpath("//*[@class='transport-check']/label/input")[random.randint(0,1)].click()
time.sleep(1)

#点击支付
driver.find_element_by_xpath("//*[@class='btn-payment']").click()
time.sleep(1.5)
driver.close()
driver.switch_to.window(h)



#随机点击现货酒款-法国
mouse3=driver.find_element_by_xpath("//*[@class='navbox']/a[2]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_elements_by_xpath("//*[@class='extend-xl']/dl//a")[random.randint(0,9)].click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#随机点击现货酒款-法国
mouse3=driver.find_element_by_xpath("//*[@class='navbox']/a[2]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_elements_by_xpath("//*[@class='extend-xl']/dl//a")[random.randint(0,9)].click()

a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#随机点击现货酒款-意大利
mouse3=driver.find_element_by_xpath("//*[@class='navbox']/a[2]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_elements_by_xpath("//*[@class='extend-xl']/div[1]//a")[random.randint(0,6)].click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#随机点击现货酒款-西班牙以下
mouse3=driver.find_element_by_xpath("//*[@class='navbox']/a[2]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_elements_by_xpath("//*[@class='extend-xl']/div[2]//a")[random.randint(0,5)].click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)


#随机点击选酒中心-产区-法国
mouse3=driver.find_element_by_xpath("//*[@class='thlink']")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
mouse3=driver.find_element_by_xpath("//*[@class='seriesnav']/dl[1]/dt")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_elements_by_xpath("//*[@class='xlzone']/dl[1]//a")[random.randint(0,10)].click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#随机点击选酒中心-产区-法国
mouse3=driver.find_element_by_xpath("//*[@class='thlink']")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
mouse3=driver.find_element_by_xpath("//*[@class='seriesnav']/dl[1]/dt")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_elements_by_xpath("//*[@class='xlzone']/dl[1]//a")[random.randint(0,10)].click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#随机点击选酒中心-产区-意大利
mouse3=driver.find_element_by_xpath("//*[@class='thlink']")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
mouse3=driver.find_element_by_xpath("//*[@class='seriesnav']/dl[1]/dt")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_elements_by_xpath("//*[@class='xlzone']/dl[2]//a")[random.randint(0,6)].click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#随机点击选酒中心-产区-意大利
mouse3=driver.find_element_by_xpath("//*[@class='thlink']")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
mouse3=driver.find_element_by_xpath("//*[@class='seriesnav']/dl[1]/dt")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_elements_by_xpath("//*[@class='xlzone']/dl[2]//a")[random.randint(0,6)].click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)


#随机点击选酒中心-意大利以下
mouse3=driver.find_element_by_xpath("//*[@class='thlink']")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
mouse3=driver.find_element_by_xpath("//*[@class='seriesnav']/dl[1]/dt")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_elements_by_xpath("//*[@class='xlzone']/div//a")[random.randint(0,11)].click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))

driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#随机点击选酒中心-意大利以下
mouse3=driver.find_element_by_xpath("//*[@class='thlink']")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
mouse3=driver.find_element_by_xpath("//*[@class='seriesnav']/dl[1]/dt")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_elements_by_xpath("//*[@class='xlzone']/div//a")[random.randint(0,11)].click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)


#随机点击选酒中心-类型
mouse3=driver.find_element_by_xpath("//*[@class='thlink']")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_elements_by_xpath("//*[@class='seriesnav']/dl[2]//a")[random.randint(0,3)].click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)


#随机点击选酒中心-品种
mouse3=driver.find_element_by_xpath("//*[@class='thlink']")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
mouse3=driver.find_element_by_xpath("//*[@class='seriesnav']/dl[3]/dt")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_elements_by_xpath("//*[@class='fgrapelist']//li//a")[random.randint(0,40)].click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#随机点击选酒中心-品种
mouse3=driver.find_element_by_xpath("//*[@class='thlink']")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
mouse3=driver.find_element_by_xpath("//*[@class='seriesnav']/dl[3]/dt")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_elements_by_xpath("//*[@class='fgrapelist']//li//a")[random.randint(0,40)].click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#随机点击选酒中心-品种
mouse3=driver.find_element_by_xpath("//*[@class='thlink']")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
mouse3=driver.find_element_by_xpath("//*[@class='seriesnav']/dl[3]/dt")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_elements_by_xpath("//*[@class='fgrapelist']//li//a")[random.randint(0,43)].click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))

driver.close()
time.sleep(0.3)
driver.switch_to.window(h)


#随机点击选酒中心-价格
mouse3=driver.find_element_by_xpath("//*[@class='thlink']")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
mouse3=driver.find_element_by_xpath("//*[@class='seriesnav']/dl[4]/dt")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_elements_by_xpath("//*[@class='priceRK']//li//a")[random.randint(0,4)].click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)


#随机点击选酒中心-评分
mouse3=driver.find_element_by_xpath("//*[@class='thlink']")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_elements_by_xpath("//*[@class='seriesnav']/dl[5]//a")[random.randint(0,2)].click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)


#点击波多尔期酒
driver.find_element_by_xpath("//*[@class='navbox']/a[4]").click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))


#期酒排序  
driver.find_element_by_xpath("//*[@class='qj-sort']/ul/li[9]").click()
time.sleep(1.5)
driver.find_element_by_xpath("//*[@class='qj-sort']/ul/li[9]").click()
time.sleep(1.5)


#期酒购买
#点击+号  将第一个商品加入购物车
driver.find_element_by_xpath("//*[@class='winelist']/dl[1]/dd/div/div/p/a[2]").click()
time.sleep(1)

driver.find_element_by_xpath("//*[@class='winelist']/dl[1]/dd/div/span").click()
time.sleep(1)


#随机选择一个商品加入购物车
driver.find_elements_by_class_name("addExpectcart")[random.randint(0,49)].click()
time.sleep(1)

#随机点击一个商品
driver.find_elements_by_class_name("lazy")[random.randint(0,49)].click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="Pay"]')))


#点击商品详情+号
driver.find_element_by_xpath("//*[@class='buy-func']/span[1]").click()
time.sleep(0.5)
#点击商品详情-号
driver.find_element_by_xpath("//*[@class='buy-func']/span[2]").click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@class='buy-func']/span[1]").click()
time.sleep(0.5)

#点击加入购物车
driver.find_element_by_xpath("//*[@id='AddCart']").click()
time.sleep(0.5)


#点击立即购买
driver.find_element_by_xpath("//*[@id='Pay']").click()
time.sleep(2)

#输入电子邮箱
driver.find_element_by_xpath("//*[@id='ReceiveEmail']").clear()
driver.find_element_by_xpath("//*[@id='ReceiveEmail']").send_keys('123@qq.com')
time.sleep(1.5)

#点击勾选协议
driver.find_element_by_xpath("//*[@id='checkexpect']").click()
time.sleep(1.5)

#点击提交订单
driver.find_element_by_xpath("//*[@id='btnToPay']").click()
time.sleep(2)

#判断是否需要积分
if driver.find_element_by_xpath('//*[@id="mask"]').get_attribute("style") == "display: block;":
    driver.close()
    driver.switch_to.window(h)
    time.sleep(1)
    driver.find_element_by_xpath("//*[@class='winelist']/dl[49]/dd/a[1]/@href").click()
    time.sleep(1.5)
    a=driver.window_handles
    driver.switch_to.window(a[1])
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='Pay']").click()
    time.sleep(1.5)
        #点击勾选协议
    driver.find_element_by_xpath("//*[@id='checkexpect']").click()
    time.sleep(1.5)
    #点击提交订单
    driver.find_element_by_xpath("//*[@id='btnToPay']").click()
    time.sleep(1.5)


#选择默认微信支付方式
#点击支付
driver.find_element_by_xpath("//*[@class='btn-payment']").click()
time.sleep(1)
driver.back()


#选择支付宝支付方式
driver.find_element_by_xpath("//*[@class='pay-zfb']").click()
time.sleep(2)
#点击支付
driver.find_element_by_xpath("//*[@class='btn-payment']").click()
time.sleep(1)
driver.back()


#选择财付通支付方式
driver.find_element_by_xpath("//*[@class='pay-cft']").click()
time.sleep(1)
#点击支付
driver.find_element_by_xpath("//*[@class='btn-payment']").click()
time.sleep(2)
driver.close()
driver.switch_to.window(h)
time.sleep(1)



#期酒搜索
driver.find_element_by_xpath("//*[@class='st-out']/input[1]").send_keys(u"拉菲")
driver.find_element_by_xpath("//*[@class='st-out']/input[2]").click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))

driver.find_element_by_xpath("//*[@class='st-out']/input[1]").clear()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))

driver.find_element_by_xpath("//*[@class='st-out']/input[2]").click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))



#随机点击选择期酒
mouse1=driver.find_element_by_xpath("//*[@class='navbox']/a[4]")
ActionChains(driver).move_to_element(mouse1).perform()
time.sleep(0.5)
s=driver.find_elements_by_xpath("//*[@class='extend-qj']/dl//a")
s[random.randint(0,15)].click()
time.sleep(0.5)

#随机点击选择期酒
mouse1=driver.find_element_by_xpath("//*[@class='navbox']/a[4]")
ActionChains(driver).move_to_element(mouse1).perform()
time.sleep(0.5)
s=driver.find_elements_by_xpath("//*[@class='extend-qj']/dl//a")
s[random.randint(0,15)].click()
time.sleep(0.5)

#点击期酒1855级庄    
driver.find_element_by_xpath("//*[@class='qj-sort']/ul/li[2]/a").click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))

#点击格拉夫列级庄   
driver.find_element_by_xpath("//*[@class='qj-sort']/ul/li[3]/a").click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))

#点击圣埃美隆级庄   
driver.find_element_by_xpath("//*[@class='qj-sort']/ul/li[4]/a").click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))

#点击波美名候级庄   
driver.find_element_by_xpath("//*[@class='qj-sort']/ul/li[5]/a").click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))

#点击中级庄级庄   
driver.find_element_by_xpath("//*[@class='qj-sort']/ul/li[6]/a").click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))

#点击苏玳列级庄级庄   
driver.find_element_by_xpath("//*[@class='qj-sort']/ul/li[7]/a").click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))

#点击右岸车库酒级庄   
driver.find_element_by_xpath("//*[@class='qj-sort']/ul/li[8]/a").click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))


#点击价格排序  
driver.find_element_by_xpath("//*[@class='qj-sort']/ul/li[9]").click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))


#点击全部期酒   
driver.find_element_by_xpath("//*[@class='qj-sort']/ul/li[1]/a").click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))




#点击跨境电商
driver.find_element_by_xpath("//*[@class='navbox']/a[3]").click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))


#跨境购买
#点击+号  将第一个商品加入购物车
driver.find_element_by_xpath("//*[@class='winelist']/dl[1]/dd/div/div/p/a[2]").click()
time.sleep(0.5)

driver.find_element_by_xpath("//*[@class='winelist']/dl[1]/dd/div/span").click()
time.sleep(0.5)


#随机选择一个商品加入购物车
driver.find_elements_by_class_name("addbtn")[random.randint(0,10)].click()
time.sleep(1)

#随机点击一个商品
driver.find_elements_by_class_name("lazy")[random.randint(0,10)].click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="Pay"]')))


#点击商品详情+号
driver.find_element_by_xpath("//*[@class='buy-func']/span[1]").click()
time.sleep(0.5)
#点击商品详情-号
driver.find_element_by_xpath("//*[@class='buy-func']/span[2]").click()
time.sleep(0.5)


#点击加入购物车
driver.find_element_by_xpath("//*[@id='AddCart']").click()
time.sleep(1)
#点击收藏
driver.find_element_by_xpath("//*[@id='store']").click()
time.sleep(3)

#点击立即购买
driver.find_element_by_xpath("//*[@id='Pay']").click()
time.sleep(5.5)

#输入身份证
edit = driver.find_element_by_class_name("edit-id")
if edit.get_attribute("style") == "display: block;":
    #点击勾选协议
    driver.find_element_by_xpath("//*[@id='ckcbp']").click()
    time.sleep(0.5)
    
else:  
# =============================================================================
#     driver.find_element_by_xpath("//*[@id='identify-num']").clear()
#     time.sleep(0.6)
# =============================================================================
    driver.find_element_by_xpath("//*[@id='identify-num']").send_keys('110101199308150012')
    time.sleep(0.6)
    driver.find_element_by_xpath("//*[@id='IDyzbtn']").click()
    time.sleep(0.5)

    #点击勾选协议
    driver.find_element_by_xpath("//*[@id='ckcbp']").click()
    time.sleep(0.5)

#点击提交订单
driver.find_element_by_xpath("//*[@id='btnToPay']").click()
time.sleep(1.5)


#判断是否需要积分
if driver.find_element_by_xpath('//*[@id="mask"]').get_attribute("style") == "display: block;":
    driver.close()
    driver.switch_to.window(h)
    time.sleep(0.5)
    driver.find_element_by_xpath("//*[@id='winelist']/dl[7]/dd/a[1]/@href").click()
    time.sleep(0.5)
    a=driver.window_handles
    driver.switch_to.window(a[1])
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="Pay"]'))).click()
   # driver.find_element_by_xpath("//*[@id='Pay']").click()
    time.sleep(1.5)
        #点击勾选协议
    driver.find_element_by_xpath("//*[@id='ckcbp']").click()
    time.sleep(0.5)
    #点击提交订单
    driver.find_element_by_xpath("//*[@id='btnToPay']").click()
    time.sleep(1.5)




#选择默认微信支付方式
#随机选择配送方式
driver.find_elements_by_xpath("//*[@class='transport-check']/label/input")[random.randint(0,1)].click()
time.sleep(0.5)

#点击支付
driver.find_element_by_xpath("//*[@class='btn-payment']").click()
time.sleep(1)
driver.back()


#选择支付宝支付方式
driver.find_element_by_xpath("//*[@class='pay-zfb']").click()
time.sleep(0.5)
#随机选择配送方式
driver.find_elements_by_xpath("//*[@class='transport-check']/label/input")[random.randint(0,1)].click()
time.sleep(0.5)
#点击支付
driver.find_element_by_xpath("//*[@class='btn-payment']").click()
time.sleep(1)
driver.back()


#选择财付通支付方式
driver.find_element_by_xpath("//*[@class='pay-cft']").click()
time.sleep(0.5)
#随机选择配送方式
driver.find_elements_by_xpath("//*[@class='transport-check']/label/input")[random.randint(0,1)].click()
time.sleep(0.5)
#点击支付
driver.find_element_by_xpath("//*[@class='btn-payment']").click()
time.sleep(2)
driver.close()
driver.switch_to.window(h)




#随机点击跨境酒款-法国
mouse2=driver.find_element_by_xpath("//*[@class='navbox']/a[3]")
ActionChains(driver).move_to_element(mouse2).perform()
time.sleep(0.5)
driver.find_elements_by_xpath("//*[@class='extend-kj']/dl//a")[random.randint(0,10)].click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))
driver.close()
time.sleep(0.5)
driver.switch_to.window(h)

#随机点击跨境酒款-法国
mouse2=driver.find_element_by_xpath("//*[@class='navbox']/a[3]")
ActionChains(driver).move_to_element(mouse2).perform()
time.sleep(0.5)
driver.find_elements_by_xpath("//*[@class='extend-kj']/dl//a")[random.randint(0,10)].click()

a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))

driver.close()
time.sleep(0.5)
driver.switch_to.window(h)

#随机点击跨境酒款-意大利以下
mouse2=driver.find_element_by_xpath("//*[@class='navbox']/a[3]")
ActionChains(driver).move_to_element(mouse2).perform()
time.sleep(0.5)
driver.find_elements_by_xpath("//*[@class='extend-kj']/div/dl//a")[random.randint(0,5)].click()

a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))

driver.close()
time.sleep(0.5)
driver.switch_to.window(h)

#跨境翻页
driver.find_element_by_xpath("//*[@class='zhtitbox']/div[1]/a[2]").click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@class='zhtitbox']/div[1]/a[1]").click()
time.sleep(0.5)


#跨境搜索框
driver.find_element_by_xpath("//*[@class='soform']/button").click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))

driver.find_element_by_xpath("//*[@class='soform']/input").send_keys(u"葡萄酒")
driver.find_element_by_xpath("//*[@class='soform']/button").click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gopage"]')))


#跨境排序
driver.find_element_by_xpath("//*[@class='left']/li[2]/a[1]").click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@class='left']/li[2]/a[1]").click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@class='left']/li[3]/a[1]").click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@class='left']/li[3]/a[1]").click()
time.sleep(1)

#跨境酒款系列
mouse2=driver.find_element_by_xpath("//*[@id='forCatena']/span")
ActionChains(driver).move_to_element(mouse2).perform()
time.sleep(0.5)
driver.find_elements_by_xpath("//*[@id='forCatena']/div/a")[(random.randint(0,17))].click()

#跨境价格区间
mouse2=driver.find_element_by_xpath("//*[@id='forPrice']/span")
ActionChains(driver).move_to_element(mouse2).perform()
time.sleep(0.5)
driver.find_elements_by_xpath("//*[@id='forPrice']/div/a")[(random.randint(0,3))].click()

#跨境评分
mouse2=driver.find_element_by_xpath("//*[@id='forScore']/span")
ActionChains(driver).move_to_element(mouse2).perform()
time.sleep(0.5)
driver.find_elements_by_xpath("//*[@id='forScore']/div/a")[(random.randint(0,4))].click()
time.sleep(1)

#跨境清空筛选
driver.find_element_by_class_name("seqReset").click()
time.sleep(1)

#点击我的订单
driver.find_element_by_xpath("//*[@class='box']/div[2]/a[2]").click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@class="pages"]')))




#首页
driver.find_element_by_xpath("//*[@class='navbox w3']/a[1]").click()
time.sleep(1)

#精品推荐更多
driver.find_element_by_xpath("//*[@class='box pad1']/div[1]/div/a[1]").click()
time.sleep(1.5)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(0.5)
driver.switch_to.window(h)

#随机点击精品推荐中的酒
driver.find_elements_by_xpath("//*[@class='box pad1']/div[1]/div[2]//dl/dd/a")[random.randint(0,5)].click()
time.sleep(1.5)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(0.5)
driver.switch_to.window(h)


#新品上线更多
driver.find_element_by_xpath("//*[@class='box pad1']/div[2]/div/a[1]").click()
time.sleep(1.5)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(0.5)
driver.switch_to.window(h)

#随机点击新品上线中的酒
driver.find_elements_by_xpath("//*[@class='box pad1']/div[2]/div[2]//dl/dd/a")[random.randint(0,5)].click()
time.sleep(1.5)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(0.5)
driver.switch_to.window(h)


#波多尔2017期酒更多
driver.find_element_by_xpath("//*[@class='box pad1']/div[2]/div/a[1]").click()
time.sleep(1.5)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(0.5)
driver.switch_to.window(h)

#随机点击新品上线中的酒
driver.find_elements_by_xpath("//*[@class='box pad1']/div[3]/div[2]//dl/dd/a")[random.randint(0,5)].click()
time.sleep(1.5)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(0.5)
driver.switch_to.window(h)

#点击轮播图一
driver.find_element_by_xpath("//*[@class='dots']/li[1]").click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='bannerAd_Div']/ul/li[1]/a/img").click()
time.sleep(1.5)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(0.5)
driver.switch_to.window(h)
#点击轮播图二
driver.find_element_by_xpath("//*[@class='dots']/li[2]").click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='bannerAd_Div']/ul/li[2]/a/img").click()
time.sleep(1.5)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(0.5)
driver.switch_to.window(h)
#点击轮播图三
driver.find_element_by_xpath("//*[@class='dots']/li[3]").click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='bannerAd_Div']/ul/li[3]/a/img").click()
time.sleep(1.5)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(0.5)
driver.switch_to.window(h)
#点击轮播图四
driver.find_element_by_xpath("//*[@class='dots']/li[4]").click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='bannerAd_Div']/ul/li[4]/a/img").click()
time.sleep(1.5)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(0.5)
driver.switch_to.window(h)
#点击轮播图五
driver.find_element_by_xpath("//*[@class='dots']/li[5]").click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='bannerAd_Div']/ul/li[5]/a/img").click()
time.sleep(1.5)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(0.5)
driver.switch_to.window(h)

#点击活动专区
driver.find_element_by_xpath("//*[@class='navbox']/a[5]").click()
time.sleep(0.5)

#点击积分换购
driver.find_element_by_xpath("//*[@class='navbox']/a[6]").click()
time.sleep(0.5)
driver.find_elements_by_xpath("//*[@class='box']/div[1]//dl//dd/a[1]")[random.randint(0,40)].click()
time.sleep(1.5)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(0.5)
driver.switch_to.window(h)

#点击中民集分宝
driver.find_element_by_xpath("//*[@class='nav-gray-group']/li[2]/a").click()
time.sleep(1)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(0.5)
driver.switch_to.window(h)

#点击酒庄品牌
driver.find_element_by_xpath("//*[@class='navbox']/a[7]").click()
time.sleep(0.5)

#点击名庄视频
driver.find_element_by_xpath("//*[@class='navbox']/a[8]").click()
time.sleep(0.5)
driver.find_elements_by_xpath("//*[@class='video']//dt/a[1]")[random.randint(0,19)].click()
time.sleep(1.5)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(0.5)
driver.switch_to.window(h)

print('结束！')

