# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 15:09:37 2018

@author: Administrator
"""
#mouse是整箱购，mouse1是搜索框，mouse2是期酒，mouse3是现货
from selenium import webdriver
import random
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

driver=webdriver.Chrome()
driver.get("http://www.wine-world.com.hk/")
time.sleep(2)
driver.find_element_by_id("q").clear()
time.sleep(1)
h=driver.current_window_handle
driver.maximize_window()
time.sleep(1)
wait = WebDriverWait(driver, 10)



#点击首页
driver.find_element_by_xpath("//*[@id='index_navlist']/a[1]").click()
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='tit-i']")))

#点击轮播图
time.sleep(0.5)
driver.find_element_by_xpath('//*[@class="dots"]/li[1]').click()

driver.find_element_by_xpath('//*[@class="box"]/div/div/ul/li[1]/a').click()

wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))
driver.back()
time.sleep(0.2)
driver.switch_to.window(h)



#新窗口打开
#点击现货更多

driver.find_element_by_xpath("//div[contains(./a[2]/text(),'现货酒款')]/a[1]/label").click()
a=driver.window_handles
driver.switch_to.window(a[1])
port_more = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))
if port_more:
    print("现货更多打开正常。")
else:
    print("现货更多打开失败！")
driver.close()
time.sleep(0.5)
driver.switch_to.window(h)


#点击期酒更多
driver.find_element_by_xpath("//*[@class='box pad1']/div/a[1]").click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))
driver.close()
time.sleep(0.5)
driver.switch_to.window(h)

#点击整箱购更多
driver.find_element_by_xpath("//*[@class='box overseas_saleProductList']/div/a[1]").click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))
driver.close()
time.sleep(0.5)
driver.switch_to.window(h)


#特惠整箱购
#点击特惠整箱购下1855列级庄 (45款)
mouse=driver.find_element_by_link_text("特惠整箱购")
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(0.3)
driver.find_element_by_xpath("//*[@id='tempalte_overseaList']/div/dl/dd[1]/a").click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#点击特惠整箱购下格拉夫列级庄 (10款)
mouse=driver.find_element_by_link_text("特惠整箱购")
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='tempalte_overseaList']/div/dl/dd[2]/a").click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#点击特惠整箱购下圣埃美隆列级庄 (11款)
mouse=driver.find_element_by_link_text("特惠整箱购")
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(0.3)
driver.find_element_by_xpath("//*[@id='tempalte_overseaList']/div/dl/dd[3]/a").click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#点击特惠整箱购下波美侯名庄 (6款)
mouse=driver.find_element_by_link_text("特惠整箱购")
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(0.3)
driver.find_element_by_xpath("//*[@id='tempalte_overseaList']/div/dl/dd[4]/a").click()
#driver.find_element_by_partial_link_text("波美侯名庄").click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)



#现货酒款
#点击法国1855列级
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[1]/dt")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_element_by_xpath("//*[@id='serCountry1']/div/a[1]").click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#点击格拉夫列级庄
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[1]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='serCountry1']/div/a[2]").click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#点击圣埃美隆列级庄
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[1]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_element_by_xpath("//*[@id='serCountry1']/div/a[3]").click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)


#点击波美侯名庄
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[1]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_element_by_xpath("//*[@id='serCountry1']/div/a[4]").click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)


#点击苏玳/巴萨克列级庄
# =============================================================================
# mouse3=driver.find_element_by_link_text("现货酒款")
# ActionChains(driver).move_to_element(mouse3).perform()
# mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[1]")
# ActionChains(driver).move_to_element(mouse3).perform()
# time.sleep(0.3)
# driver.find_element_by_xpath("//*[@id='serCountry1']/div/a[5]").click()
# time.sleep(2)
# a=driver.window_handles
# driver.switch_to.window(a[1])
# driver.close()
# time.sleep(0.3)
# driver.switch_to.window(h)
# 
# =============================================================================
#点击勃艮第特级园
# =============================================================================
# mouse3=driver.find_element_by_link_text("现货酒款")
# ActionChains(driver).move_to_element(mouse3).perform()
# mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[1]")
# ActionChains(driver).move_to_element(mouse3).perform()
# time.sleep(0.3)
# driver.find_element_by_xpath("//*[@id='serCountry1']/div/a[6]").click()
# time.sleep(2)
# a=driver.window_handles
# driver.switch_to.window(a[1])
# driver.close()
# time.sleep(0.3)
# driver.switch_to.window(h)
# =============================================================================

#点击勃艮第一级园
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[1]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_element_by_xpath("//*[@id='serCountry1']/div/a[7]").click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#点击勃艮第金丘名村
# =============================================================================
# mouse3=driver.find_element_by_link_text("现货酒款")
# ActionChains(driver).move_to_element(mouse3).perform()
# mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[1]")
# ActionChains(driver).move_to_element(mouse3).perform()
# time.sleep(0.3)
# driver.find_element_by_xpath("//*[@id='serCountry1']/div/a[8]").click()
# time.sleep(2)
# a=driver.window_handles
# driver.switch_to.window(a[1])
# driver.close()
# time.sleep(0.3)
# driver.switch_to.window(h)
# =============================================================================

#点击罗讷河谷名庄
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[1]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_element_by_xpath("//*[@id='serCountry1']/div/a[9]").click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#点击超级托斯卡纳
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[2]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_element_by_xpath("//*[@id='tempalte_spotList']/div[2]/div[2]/div/a[1]").click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#点击意大利巴罗洛
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[2]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_element_by_xpath("//*//*[@id='tempalte_spotList']/div[2]/div[2]/div/a[2]").click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#点击意大利巴巴莱斯科
# =============================================================================
# mouse3=driver.find_element_by_link_text("现货酒款")
# ActionChains(driver).move_to_element(mouse3).perform()
# mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[2]")
# ActionChains(driver).move_to_element(mouse3).perform()
# time.sleep(0.3)
# driver.find_element_by_xpath("//*[@id='tempalte_spotList']/div[2]/div[2]/div/a[3]").click()
# time.sleep(2)
# a=driver.window_handles
# driver.switch_to.window(a[1])
# driver.close()
# time.sleep(0.3)
# driver.switch_to.window(h)
# =============================================================================

#点击意大利布鲁奈罗
# =============================================================================
# mouse3=driver.find_element_by_link_text("现货酒款")
# ActionChains(driver).move_to_element(mouse3).perform()
# mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[2]")
# ActionChains(driver).move_to_element(mouse3).perform()
# time.sleep(0.3)
# driver.find_element_by_xpath("//*[@id='tempalte_spotList']/div[2]/div[2]/div/a[4]").click()
# time.sleep(2)
# a=driver.window_handles
# driver.switch_to.window(a[1])
# driver.close()
# time.sleep(0.3)
# driver.switch_to.window(h)
# =============================================================================

#点击意大利经典基安帝
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[2]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_element_by_xpath("//*[@id='tempalte_spotList']/div[2]/div[2]/div/a[5]").click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#点击意大利名庄
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[2]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_element_by_xpath("//*[@id='tempalte_spotList']/div[2]/div[2]/div/a[6]").click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#点击西班牙名庄
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[3]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_element_by_xpath("//*[@id='tempalte_spotList']/div[2]/div[3]/div/a[1]").click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#点击美国名庄
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[4]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_element_by_xpath("//*[@id='tempalte_spotList']/div[2]/div[4]/div/a[1]").click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#点击智利名庄
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[5]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(0.3)
driver.find_element_by_xpath("//*[@id='tempalte_spotList']/div[2]/div[5]/div/a[1]").click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)


#随机点击现货酒款中的酒
driver.find_elements_by_xpath("//*[@class='winebox']//div/dl/dt/a")[random.randint(0,4)].click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='account']")))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#随机点击波多尔期酒中的酒
driver.find_elements_by_xpath("//*[@class='winebox future_saleProductList']//div//div/dl/dt/a")[random.randint(0,8)].click()

a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='account']")))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)

#随机点击现整箱购中的酒
driver.find_elements_by_xpath("//*[@class='winebox']//div/dl/dt/a")[random.randint(0,9)].click()
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='account']")))
driver.close()
time.sleep(0.3)
driver.switch_to.window(h)



#点击进入购物车
driver.find_element_by_xpath("//*[@class='nav-cart']").click()
time.sleep(1)
driver.back()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@class='wcartbtn']").click()
time.sleep(2)

#删除第一个现货商品
driver.find_element_by_xpath("//*[@class='cartbox']/div[2]/dl/dd[4]/div/span[1]").click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@class='cartbox']/div[2]/dl/dd[4]/div/span[2]").click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@class='cartbox']/div[2]/dl/dd[7]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@class='layui-layer-btn0']").click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@class='layui-layer-btn0']").click()
time.sleep(0.5)


#切换到整箱购
driver.find_element_by_xpath("//*[@class='cart-sort']/span[2]").click()
time.sleep(0.5)

#切换到期酒
driver.find_element_by_xpath("//*[@class='cart-sort']/span[3]").click()
time.sleep(0.5)

#切换到现货,点击购买
driver.find_element_by_xpath("//*[@class='cart-sort']/span[1]").click()
time.sleep(1.5)
driver.find_element_by_xpath("//*[@id='SPOT']/div[2]/dl/dt/label").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@class='buy-btn']").click()
time.sleep(1)

#选择微信支付
driver.find_element_by_xpath("//*[@class='paylist']/div[4]/img").click()
time.sleep(1.5)
driver.find_element_by_xpath("//*[@class='buy-btn']").click()















#登陆
signInBut = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="signIn"]')))
signInBut.click()
# =============================================================================
# driver.find_element_by_xpath("//*[@id='signIn']").click()
# time.sleep(1.5)
# =============================================================================

driver.find_element_by_xpath("//*[@id='userName']").send_keys("18700000083")


driver.find_element_by_xpath("//*[@id='password']").send_keys("123456")
time.sleep(1)

driver.find_element_by_xpath("//*[@id='btnSignIn']").click()
time.sleep(2)


#点击导航栏特惠整箱购
driver.find_element_by_xpath("//*[@id='index_navlist']/a[3]").click()
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))
driver.find_element_by_xpath("//*[@id='index_navlist']/a[3]").click()
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='page-btn']")))


driver.find_element_by_xpath("//*[@id='productListBox']/div[2]/div[2]/dl[2]/dd/div/div/p/span[3]").click()
time.sleep(1)

driver.find_element_by_xpath("//*[@id='productListBox']/div[2]/div[2]/dl[2]/dd/div/div/p/span[1]").click()
time.sleep(1)

driver.find_element_by_xpath("//*[@id='productListBox']/div[2]/div[2]/dl[2]/dd/div/span").click()
time.sleep(1)


#随机选择一个商品加入购物车
driver.find_elements_by_class_name("addbtn")[random.randint(0,49)].click()
time.sleep(1.5)

#随机点击一个商品
driver.find_elements_by_xpath("//*[@class='wl']//dl//a")[random.randint(0,149)].click()
time.sleep(1.5)
a=driver.window_handles
driver.switch_to.window(a[1])
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='account']")))

#点击商品详情+号
driver.find_element_by_xpath("//*[@class='buy-plus']").click()
time.sleep(0.5)
#点击商品详情-号
driver.find_element_by_xpath("//*[@class='buy-minus']").click()
time.sleep(0.5)

#获取整箱购价格
oversea_price = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="page"]/body/div[9]/div[2]/div[4]/div/span[2]/i'))).text


if oversea_price:
    oversea_price = int(oversea_price.replace('/瓶',''))
    print(oversea_price)
#点击加入购物车
driver.find_element_by_xpath("//*[@class='addcart']").click()
time.sleep(0.5)

#点击立即购买
driver.find_element_by_xpath("//*[@class='account']").click()
time.sleep(1.8)
a=driver.window_handles
driver.switch_to.window(a[2])



z_oversea_price = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="page"]/body/div[4]/div[7]/dl[2]/dd[2]/label'))).text

if float(z_oversea_price) == float(oversea_price) * 0.95:
    print('整箱购价格正确')
#选择银联支付
    driver.find_element_by_xpath("//*[@class='paylist']/div[1]/img").click()
    time.sleep(0.5)
else:
    print('整箱购价格错误')




#勾选协议
driver.find_element_by_xpath("//*[@id='checkbox3']").click()
time.sleep(0.5)

#点击
driver.find_element_by_xpath("//*[@class='buy-btn']").click()
time.sleep(4)
driver.close()
time.sleep(1)
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)







#点击导航栏现货酒款
driver.find_element_by_xpath("//*[@class='haiwai']/a[1]").click()
time.sleep(5)

#点击+号  将第一个商品加入购物车
driver.find_element_by_xpath("//*[@id='productListBox']/div[2]/div[2]/dl[1]/dd/div/div/p/span[3]").click()
time.sleep(0.5)

driver.find_element_by_xpath("//*[@id='productListBox']/div[2]/div[2]/dl[1]/dd/div/span").click()
time.sleep(0.5)


#随机选择一个商品加入购物车
driver.find_elements_by_class_name("addbtn")[random.randint(0,49)].click()
time.sleep(1.5)

#随机点击一个商品
driver.find_elements_by_xpath("//*[@class='wl']//dl//a")[random.randint(0,149)].click()
time.sleep(1.5)
a=driver.window_handles
driver.switch_to.window(a[1])
time.sleep(1)

#点击商品详情+号
driver.find_element_by_xpath("//*[@id='page']/body/div[9]/div[2]/div[7]/div[3]/span[1]").click()
time.sleep(0.5)
#点击商品详情-号
driver.find_element_by_xpath("//*[@id='page']/body/div[9]/div[2]/div[7]/div[3]/span[2]").click()
time.sleep(0.5)

#点击加入购物车
driver.find_element_by_xpath("//*[@class='addcart']").click()
time.sleep(0.5)

#获取酒款价格
spot_price = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="page"]/body/div[9]/div[2]/div[4]/div/span[2]/i'))).text
print(spot_price)
print(int(spot_price))
print(int(0.95))
ccc=int(spot_price)*0.95
print(ccc)

#点击立即购买
driver.find_element_by_xpath("//*[@class='account']").click()
time.sleep(2)
a=driver.window_handles
driver.switch_to.window(a[2])
time.sleep(1)

#获取订单确认页面折后价格
z_spot_price = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="page"]/body/div[4]/div[7]/dl[2]/dd[2]/label'))).text
print(z_spot_price)

if float(z_spot_price) == float(spot_price) * 0.95:
    print('现货价格正确')
#选择支付宝支付
    driver.find_element_by_xpath("//*[@class='paylist']/div[2]/img").click()
    time.sleep(0.5)
else:
    print('价格错误')


#点击确认，再关闭
driver.find_element_by_xpath("//*[@class='buy-btn']").click()
time.sleep(3)
driver.close()
time.sleep(1)
driver.switch_to.window(a[1])


#点击立即购买
driver.find_element_by_xpath("//*[@class='account']").click()
time.sleep(1.5)
a=driver.window_handles
driver.switch_to.window(a[2])
time.sleep(1)


#悬浮选购中心
# =============================================================================
# mouse=driver.find_element_by_link_text("现货酒款")
# ActionChains(driver).move_to_element(mouse).perform()
# time.sleep(1)
# =============================================================================
#排序筛选下一页
driver.find_element_by_id("q").send_keys(u"葡萄酒")
time.sleep(1)
driver.find_element_by_tag_name("button").click()
time.sleep(4)
#产区筛选
s=driver.find_elements_by_xpath("//*[@class='retrieval']/dl[2]/dd/a")
s[random.randint(1, 7)].click()
time.sleep(3)
driver.find_element_by_xpath("//*[@class='retrieval']/dl[2]/dd/a[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@class='retrieval']/dl[2]/dd/a[1]").click()
time.sleep(5)

#品种筛选
s=driver.find_elements_by_xpath("//*[@class='retrieval']/dl[3]/dd/a")
s[random.randint(1, 23)].click()
time.sleep(5)
driver.find_element_by_xpath("//*[@class='retrieval']/dl[3]/dd/a[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@class='retrieval']/dl[3]/dd/a[1]").click()
time.sleep(5)

#价格筛选
s=driver.find_elements_by_xpath("//*[@class='retrieval']/dl[4]/dd/a")
s[random.randint(1, 7)].click()
time.sleep(5)
driver.find_element_by_xpath("//*[@class='retrieval']/dl[4]/dd/a[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@class='retrieval']/dl[4]/dd/a[1]").click()
time.sleep(5)

#系列筛选
s=driver.find_elements_by_xpath("//*[@class='retrieval']/dl[5]/dd/a")
s[random.randint(1, 20)].click()
time.sleep(5)
s=driver.find_element_by_xpath("//*[@class='retrieval']/dl[5]/dd/a[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@class='retrieval']/dl[5]/dd/a[1]").click()
time.sleep(5)

#重置
driver.find_element_by_xpath("//*[contains(@class,'reset-xj')]").click()
time.sleep(5)

#排序
driver.find_element_by_xpath("//*[@id='ranklist']/a[2]/span").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='ranklist']/a[2]/span").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='ranklist']/a[3]/span").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='ranklist']/a[3]/span").click()
time.sleep(5)
#翻页
driver.find_element_by_xpath("//*[@id='fanye']/a[1]").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='fanye']/a[1]").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='fanye']/a[2]").click()
time.sleep(5)

#搜索框默认选择现货，输入拉菲古点击
driver.find_element_by_id("q").clear()
time.sleep(1)
driver.find_element_by_id("q").send_keys(u"拉菲古")
time.sleep(1)
driver.find_element_by_tag_name("button").click()
time.sleep(2)

#搜索框选择期酒，点击搜索
mouse2=driver.find_element_by_class_name("soption")
ActionChains(driver).move_to_element(mouse2).perform()
time.sleep(2)

driver.find_element_by_xpath("//*[@class='sp-downlist']/li[2]").click()
driver.find_element_by_tag_name("button").click()
time.sleep(2)

#搜索框选择整箱购，点击搜索
mouse2=driver.find_element_by_class_name("soption")
ActionChains(driver).move_to_element(mouse2).perform()
time.sleep(2)
 
driver.find_element_by_xpath("//*[@class='sp-downlist']/li[3]").click()
driver.find_element_by_tag_name("button").click()
time.sleep(2)


#点击导航栏现货酒款
driver.find_element_by_xpath("//*[@class='haiwai']/a[1]").click()
time.sleep(5)

#点击导航栏波多尔期酒
driver.find_element_by_xpath("//*[@id='index_navlist']/a[2]").click()
time.sleep(4)

#点击导航栏特惠整箱购
driver.find_element_by_xpath("//*[@id='index_navlist']/a[3]").click()
time.sleep(4)



#点击期酒下的波美名候列级庄
mouse1=driver.find_element_by_xpath("//*[@id='index_navlist']/a[2]")
ActionChains(driver).move_to_element(mouse1).perform()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='tempalte_futureList']/div/dl/dd[1]/a").click()
time.sleep(1)

#点击期酒下的1855列级庄
mouse1=driver.find_element_by_xpath("//*[@id='index_navlist']/a[2]")
ActionChains(driver).move_to_element(mouse1).perform()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='tempalte_futureList']/div/dl/dd[2]/a").click()
time.sleep(1)

#点击期酒下的圣埃美隆列级庄
mouse1=driver.find_element_by_xpath("//*[@id='index_navlist']/a[2]")
ActionChains(driver).move_to_element(mouse1).perform()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='tempalte_futureList']/div/dl/dd[3]/a").click()
time.sleep(1)

#点击期酒下的格拉夫列级庄
mouse1=driver.find_element_by_xpath("//*[@id='index_navlist']/a[2]")
ActionChains(driver).move_to_element(mouse1).perform()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='tempalte_futureList']/div/dl/dd[4]/a").click()
time.sleep(1)


#点击首页
driver.find_element_by_xpath("//*[@id='index_navlist']/a[1]").click()
time.sleep(2)




#新窗口打开
#点击现货更多
driver.find_element_by_xpath("//*[@class='box pad1 spot_saleProductList']/div/a[1]").click()
time.sleep(5)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)


#点击期酒更多
driver.find_element_by_xpath("//*[@class='box pad1']/div/a[1]").click()
time.sleep(5)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)

#点击整箱购更多
driver.find_element_by_xpath("//*[@class='box overseas_saleProductList']/div/a[1]").click()
time.sleep(5)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)


#特惠整箱购
#点击特惠整箱购下1855列级庄 (45款)
mouse=driver.find_element_by_link_text("特惠整箱购")
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='tempalte_overseaList']/div/dl/dd[1]").click()
time.sleep(2)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)

#点击特惠整箱购下格拉夫列级庄 (10款)
mouse=driver.find_element_by_link_text("特惠整箱购")
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='tempalte_overseaList']/div/dl/dd[2]").click()
time.sleep(2)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)

#点击特惠整箱购下圣埃美隆列级庄 (11款)
mouse=driver.find_element_by_link_text("特惠整箱购")
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='tempalte_overseaList']/div/dl/dd[3]").click()
time.sleep(2)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)

#点击特惠整箱购下波美侯名庄 (6款)
mouse=driver.find_element_by_link_text("特惠整箱购")
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='tempalte_overseaList']/div/dl/dd[4]/a").click()
#driver.find_element_by_partial_link_text("波美侯名庄").click()
time.sleep(2)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)




#现货酒款
#点击法国1855列级
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[1]/dt")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='serCountry1']/div/a[1]").click()
time.sleep(4)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)

#点击格拉夫列级庄
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[1]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='serCountry1']/div/a[2]").click()
time.sleep(2)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)

#点击圣埃美隆列级庄
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[1]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='serCountry1']/div/a[3]").click()
time.sleep(2)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)


#点击波美侯名庄
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[1]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='serCountry1']/div/a[4]").click()
time.sleep(2)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)


#点击苏玳/巴萨克列级庄
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[1]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='serCountry1']/div/a[5]").click()
time.sleep(2)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)

#点击勃艮第特级园
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[1]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='serCountry1']/div/a[6]").click()
time.sleep(2)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)

#点击勃艮第一级园
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[1]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='serCountry1']/div/a[7]").click()
time.sleep(2)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)

#点击勃艮第金丘名村
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[1]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='serCountry1']/div/a[8]").click()
time.sleep(2)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)

#点击罗讷河谷名庄
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[1]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='serCountry1']/div/a[9]").click()
time.sleep(2)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)

#点击超级托斯卡纳
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[2]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='tempalte_spotList']/div[2]/div[2]/div/a[1]").click()
time.sleep(2)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)

#点击意大利巴罗洛
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[2]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(1)
driver.find_element_by_xpath("//*//*[@id='tempalte_spotList']/div[2]/div[2]/div/a[2]").click()
time.sleep(2)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)

#点击意大利巴巴莱斯科
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[2]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='tempalte_spotList']/div[2]/div[2]/div/a[3]").click()
time.sleep(2)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)

#点击意大利布鲁奈罗
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[2]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='tempalte_spotList']/div[2]/div[2]/div/a[4]").click()
time.sleep(2)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)

#点击意大利经典基安帝
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[2]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='tempalte_spotList']/div[2]/div[2]/div/a[5]").click()
time.sleep(2)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)

#点击意大利名庄
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[2]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='tempalte_spotList']/div[2]/div[2]/div/a[6]").click()
time.sleep(2)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)

#点击西班牙名庄
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[3]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='tempalte_spotList']/div[2]/div[3]/div/a[1]").click()
time.sleep(2)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)

#点击美国名庄
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[4]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='tempalte_spotList']/div[2]/div[4]/div/a[1]").click()
time.sleep(2)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.close()
time.sleep(1)
driver.switch_to.window(h)

#点击智利名庄
mouse3=driver.find_element_by_link_text("现货酒款")
ActionChains(driver).move_to_element(mouse3).perform()
mouse3=driver.find_element_by_xpath("//*[@id='hwnav']/dl[5]")
ActionChains(driver).move_to_element(mouse3).perform()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='tempalte_spotList']/div[2]/div[5]/div/a[1]").click()
time.sleep(2)
# =============================================================================
# a=driver.window_handles
# driver.switch_to.window(a[1])
# driver.close()
# time.sleep(1)
# driver.switch_to.window(h)
# =============================================================================


# =============================================================================
# driver.set_window_size(540,540)
# time.sleep(2)
# driver.maximize_window()
# =============================================================================
#driver.close()