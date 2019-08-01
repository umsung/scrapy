import json
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
import re
import requests
from bs4 import BeautifulSoup
import pymongo
import time

heeders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'referer': 'www.jd.com'
}

# 启动Chrome Headless 无界面模式
chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# 启动浏览器，获取网页源代码
browser = webdriver.Chrome()
# 启动phantomJs 无界面
# browser = webdriver.PhantomJS()
wait = WebDriverWait(browser, 6)
h = browser.current_window_handle
browser.execute_script('window.open()')   # 打开新的标签页码
handles = browser.window_handles
browser.switch_to.window(h)

# 定义入口查询界面
def search():
    browser.get('https://www.jd.com/')


    try:
        # 查找搜索框及搜索按钮，输入信息并点击按钮
        input = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#key")))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#search > div > div.form > button")))
        input[0].send_keys('手机')
        submit.click()
        # 获取总页数
        page = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > em:nth-child(1) > b')))
        return page[0].text
    # 如果异常，递归调用本函数
    except TimeoutException:
        search()


# 翻页
def next_page(page_number):
    try:
        # # 滑动到网页底部，加载出所有商品信息
        # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(4)
        # html = browser.page_source
        # 当网页到达100页时，下一页按钮失效，所以选择结束程序
        # while page_number == 101:
        #     exit()
        # 查找下一页按钮，并点击按钮

        while page_number == 101:
            exit()
        links = parse_html()
        a = next(links)
        b = next(links)
        # for link in links:
        print('当前爬取的页面：', a)
        # product_id = re.search(r"\d+", a).group()
        # result = get_price(product_id)
        # print(result)
        browser.switch_to.window(handles[1])
        detail_html = detail_page(a)
        c = detail_page(b)
        get_detail(detail_html)

        browser.switch_to.window(h)
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.pn-next > em')))
        button.click()
        # 判断是否加载到本页最后一款产品Item(每页显示60条商品信息)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#J_goodsList > ul > li:nth-child(60)")))
        # 判断翻页成功
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#J_bottomPage > span.p-num > a.curr"), str(page_number)))
        # return html

    except TimeoutException:
        return next_page(page_number)


# 解析每一页面上的a链接
def parse_html():
    """
    解析商品列表网页,获取商品的详情页
    """
    # 滑动到网页底部，加载出所有商品信息
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)
    html = browser.page_source

    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select('.gl-item')
    for item in items:
        a = item.select('.p-name.p-name-type-2 a')
        link = str(a[0].attrs['href'])
        if 'https:' in link:
            continue
        else:
            link = "https:"+link
        yield link


# 进入详情页
def detail_page(link):
    """
    进入item详情页
    :param link: item link
    :return: html
    """
    browser.get(link)
    try:
        # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        html = browser.page_source
        return html
    except TimeoutException:
        detail_page(link)


# 获取详情页的手机信息
def get_detail(html):
    """
    获取详情页的数据
    :param html:
    :return:
    """
    dic ={}
    soup = BeautifulSoup(html, 'html.parser')
    item_list = soup.find_all('div', class_='Ptable-item')
    for item in item_list:
        contents1 = item.findAll('dt')
        contents2 = item.findAll('dd')
        for i in range(len(contents1)):
            dic[contents1[i].string] = contents2[i].string

    # dic['price_jd '] = result[0]['p']
    # dic['price_mk '] = result[0]['m']
    print(dic)
    save_mongo(dic)


# 获取手机价格，由于价格信息是请求另外一个地址https://p.3.cn/prices/mgets?skuIds=7340016
def get_price(product_id):
    url = 'https://p.3.cn/prices/mgets?skuIds=J_' + product_id
    response = requests.get(url,heeders)
    result = json.loads(response.text)
    return result


# 存储到mongoDB
def save_mongo(dic):
    # 创建连接对象
    client = pymongo.MongoClient(host='localhost', port=27017)
    # 指定数据库
    db = client['jd']
    # 声明Collection对象
    collection = db['phone']
    collection.insert_one(dic)


def main():
    page = search()
    total = int(page)
    print(total)
    for i in range(2, total+2):
        time.sleep(5)
        print("第", i-1, "页：")
        next_page(i)

        # html = next_page(i)
        # links = parse_html()
        # a = next(links)
        # # for link in links:
        # print('当前爬取的页面：', a)
        # product_id = re.search(r"\d+", a).group()
        # # result = get_price(product_id)
        # # print(result)
        # detail_html = detail_page(a)
        # get_detail(detail_html)


if __name__ == "__main__":
    main()