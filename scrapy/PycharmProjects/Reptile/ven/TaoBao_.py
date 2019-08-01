from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from bs4 import BeautifulSoup
import requests
import os
import csv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# 设置Useragent
# dcpa = dict(DesiredCapabilities.CHROME)
# dcap["chrome.page.settings.userAgent"] = "Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
# broswer = webdriver.Chrome(desired_capabilities=dcap)


#这种更好
# option = webdriver.ChromeOptions()
# # chrome_options = Options()
# 无头模式启动
# option.add_argument('--headless')
# 谷歌文档提到需要加上这个属性来规避bug
# option.add_argument('--disable-gpu')
# 禁用图片
# chrome_options.add_argument('blink-settings=imagesEnabled=false')
# 修改User-Agent
# chrome_options.add_argument('user-agent= '你想修改成的User-Agent')
# 添加代理
# chrome_options.add_argument("--proxy-server=http://" + ip：port)

# 初始化实例
# broswer = webdriver.Chrome(options=option)




broswer = webdriver.Chrome()
wait = WebDriverWait(broswer, 15)


def search():
    try:
        broswer.get('https://www.taobao.com/')
        # print(broswer.get_cookies())
        # broswer.delete_all_cookies()
        #
        # for i in cookies:
        #     if i['domain'][:1] in broswer.current_url:
        #         broswer.add_cookie(i)
        # broswer.refresh()
        print(broswer.get_cookies())
        inp = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        inp.send_keys(u'美食')
        submit.click()
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))
        return total.text
    except TimeoutError:
        return search()


def next_page(page_num):
    try:
        inp = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        inp.clear()
        inp.send_keys(page_num)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_num)))
        print('正在下载第{}页'.format(page_num))
        parse_page_index()
        for i in parse_page_index():
            print(i)
            download_img(i[0], i[5])
            sav_data().writerow(i)
    except TimeoutError:
        next_page(page_num)


def parse_page_index():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    html = broswer.page_source
    soup = BeautifulSoup(html, 'lxml')
    items = soup.select('div.items > div.item')
    for item in items:
        yield [
            'http:' + item.find('img', class_='J_ItemPic img').get('data-src'),
            item.find('img', class_='J_ItemPic img').get('alt'),
            item.find('div', class_='price g_price g_price-highlight').find('strong').text,
            item.find('div', class_='deal-cnt').text,
            item.find('span', class_='dsrs').find_next_sibling().text,
            item.find('a', class_='pic-link J_ClickStat J_ItemPicA').get('data-nid')
        ]


def download_img(url, name):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            return sav_img(resp.content, name)
        return None
    except ConnectionError:
        print("error connect")
        return None


def sav_img(img_url, img_name):
    try:
        os.mkdir('taobao')
    except FileExistsError:
        pass
    with open(r'./taobao/{}.jpg'.format(img_name), 'wb') as f:
        f.write(img_url)
        f.close()


def sav_data():
    f = open('taobao.csv', 'a', encoding='utf-8', newline='')
    w = csv.writer(f)
    return w


def main():
    total = search()
    sum_page_num = int(re.search(r'(\d+)', total, re.S).group(1))
    for page_num in range(1, sum_page_num+1):
        next_page(page_num)
    # print(search())

    # search()
    # parse_page_index()


if __name__ == '__main__':
    main()