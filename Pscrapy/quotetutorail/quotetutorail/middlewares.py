# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import datetime
import json
import logging
import random
import time
from cmath import e
from fake_useragent import UserAgent
import requests
from scrapy import signals
from scrapy.exceptions import IgnoreRequest
from scrapy.http import HtmlResponse
from quotetutorail.quotetutorail.settings import IPPOOL
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import scrapy

# Downloader Middleware处理的过程主要在调度器发送requests请求的时候以及网页将response结果返回给spiders的时候
# 代理cookies池 中间件, 用于登陆，登陆的账号操作久了会被封，账号被封，换ip也没用
class CookiesMiddleWare(object):
    def __init__(self, cookies_pool_url):
        self.logger = logging.getLogger(__name__)
        self.cookies_pool_url = cookies_pool_url

    # 随机获取cookies_pool_url中的cookies，cookies_pool_url是api接口，cookies池
    def _get_random_cookies(self):
        try:
            response = requests.get(self.cookies_pool_url)
            if response.status_code == 200:
                return json.loads(response.text)
        except ConnectionError:
            return None

    # 此方法是修改requests请求
    def process_request(self, request, spider):
        cookies = self._get_random_cookies()
        if cookies:
            request.cookies = cookies
            self.logger.debug('Using Cookies ' + json.dumps(cookies))
        else:
            self.logger.debug('No Valid Cookies')

    # 类方法获取setting中的配置信息
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            cookies_pool_url=crawler.settings.get('COOKIES_POOL_URL')
        )

    # 此方法是处理response响应
    def process_response(self, request, response, spider):
        # 携带cookies请求，可能会出现cookies失效的情况。访问失败会出现两种情况：
        # 1、重定向302到验证码页面。 2、直接封锁账号，404
        # 拦截重定向，在setting中配置allow_redirect=false

        if response.status in [300, 301, 302, 303]:
            try:
                redirect_url = response.headers['location']
                if 'login.weibo' in redirect_url or 'login.sina' in redirect_url:  # Cookie失效
                    self.logger.warning('Updating Cookies')
                elif 'weibo.cn/security' in redirect_url:
                    self.logger.warning('Now Cookies' + json.dumps(request.cookies))
                    self.logger.warning('One Account is locked!')

                # 出现封锁或者重定向，说明请求失败，需要重新获取cookies更换
                request.cookies = self._get_random_cookies()
                self.logger.debug('Using Cookies' + json.dumps(request.cookies))
                # 返回值request： 停止后续的response中间件，将request重新放入调度器的队列重新请求
                return request
            except Exception:
                raise IgnoreRequest
        elif response.status in [414]:
            return request
        else:
            # 如果没有出现封锁或重定向，直接将response向下传递给后续的中间件
            return response


# 代理ip池 中间件
class ProxyMiddleWare(object):
    """docstring for ProxyMiddleWare"""
    def __init__(self, proxy_pool_url):
        self.PROXY_POOL_URL = proxy_pool_url

    def process_request(self, request, spider):
        '''对request对象加上proxy'''
        proxy = self.get_random_proxy()
        print("this is request ip:" + proxy)
        request.meta['proxy'] = 'http://' + proxy

    def process_response(self, request, response, spider):
        '''对返回的response处理'''
        # 如果返回的response状态不是200，重新生成当前request对象
        if response.status != 200:
            proxy = self.get_random_proxy()
            print("this is response ip:" + proxy)
            # 对当前requests加上代理
            request.meta['proxy'] = 'http://' + proxy
            return request
        return response

    def get_random_proxy(self):
        '''随机从文件中读取proxy'''
        while 1:
            with open('proxies.txt', 'r') as f:
                proxies = f.readlines()
            if proxies:
                break
            else:
                time.sleep(1)
        proxy = random.choice(proxies).strip()
        return proxy

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            proxy_pool_url=crawler.settings.get('PROXY_POOL_URL')
        )

    def _get_random_proxt(self):
        try:
            resp = requests.get(self.PROXY_POOL_URL)    # 通过ip代理池返回ip
            if resp.status_code == 200:
                return resp.text
        except ConnectionError:
            return None


class RandomUserAgentMiddleware(object):
    def __init__(self, c):
        super(RandomUserAgentMiddleware, self).__init__()
        self.ua = UserAgent()
        self.random_ua_type = c.settings.get('RANDOM_UA_TYPE', 'random')  # settings中有'RANDOM_UA_TYPE'就去这个值，没有就取random

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def get_ua(self):
        return getattr(self.ua, self.random_ua_type)

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', self.get_ua())

class RandomUserAgentMiddleware2(object):
    def __init__(self, user_agents):
        self.user_agents = user_agents

    @classmethod
    def from_crawler(cls, crawler):
        s = cls(crawler.settings.get('MY_USER_AGENT'))
        return s
    
    def process_request(self, request, spider):
        request.header['User-Agent'] = random.choice(self.user_agents)
        return None

class WeatherSpiderDownloaderMidderware(object):
    def process_request(self,request, spider):
        if request.meta.get('selenium'):
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            driver = webdriver.chrome(chrome_options=chrome_options)
            driver.get(request.url)
            time.sleep(1)
            html = driver.page_source
            driver.quit()
            return HtmlResponse(url=request.url,body=html,encoding='utf-8',request=request)
        return None

class QuotetutorailSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class QuotetutorailDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called

        return None


    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class PayLoadRequestMiddleware(object):

    def process_request(self, request, spider):
        # 如果有的请求是带有payload请求的，在这个里面处理掉
        if request.meta.get('payloadFlag', False):
            print(f"PayLoadRequestMiddleware enter")
            postUrl = request.url
            headers = request.meta.get('headers', {})
            payloadData = request.meta.get('payloadData', {})
            # proxy = request.meta['proxy']
            # proxies = {
            #     "http": proxy,
            #     "https": proxy,
            # }
            timeOut = request.meta.get('download_timeout', 25)
            allow_redirects = request.meta.get('dont_redirect', False)
            dumpJsonData = json.dumps(payloadData)
            print(f"dumpJsonData = {dumpJsonData}")
            # 发现这个居然是个同步 阻塞的过程，太过影响速度了
            res = requests.post(postUrl, data=dumpJsonData, headers=headers, timeout=timeOut,
                                allow_redirects=allow_redirects)
            # res = requests.post(postUrl, json=payloadData, headers=header)
            print(f"responseTime = {datetime.datetime.now()}, res text = {res.text}, statusCode = {res.status_code}")
            if res.status_code > 199 and res.status_code < 300:
                # 返回Response，就进入callback函数处理，不会再去下载这个请求
                return HtmlResponse(url=request.url,
                                    body=res.content,
                                    request=request,
                                    # 最好根据网页的具体编码而定
                                    encoding='utf-8',
                                    status=200)
            else:
                print(f"request mode getting page error, Exception = { e }")
                return HtmlResponse(url=request.url, status=500, request=request)


class RandomUserAgentMiddleware(object):
    '''
    随机更换User-Agent
    '''
    def __init__(self, crawler):
        super(RandomUserAgentMiddleware, self).__init__()
        self.ua =  ()
        self.ua_type = crawler.settings.get('RANDOM_UA_TYPE', 'random')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):

        def get_ua():
            return getattr(self.ua, self.ua_type)
        request.headers.setdefault('User-Agent', get_ua())


class ProxychiMiddleware(object):
    # logger = logging.getLogger(__name__)

    # 定义一个请求之前的方法
    def process_request(self, request, spider):
        # 如果是 私密代理
        # request.meta['proxy'] = 'https://用户名and密码114.212.12.4:3128'
        # 随即获取一个代理
        # this_ip = random.choice
        # self.logger.debug("Using Proxy")

        request.meta['proxy'] = 'https://61.164.39.68:53281'

        return None

    # def process_exception(self, request, exception, spider):
    #     # 当请求遇到错误后（现因为频繁爬取被封ip后） 就会随机选择ip继续访问
    #     # self.logger.info("GET Exception")
    #     # 如果是 私密代理
    #     # request.meta['proxy'] = 'https://用户名:密码@114.212.12.4:3128'
    #     # 随即获取一个代理
    #     this_ip = random.choice(IPPOOL)
    #     request.meta['proxy'] = 'HTTP://' + this_ip['ipaddr']
    #     return request





class JSPageMiddleware(object):
    def __init__(self):  # 使用同一个self，保证只打开一个浏览器，所有spider使用一个浏览器
        self.browser = webdriver.Chrome(executable_path="C:/Program Files/Google/Chrome/Application/chromedriver.exe")
        super(JSPageMiddleware, self).__init__()

    # 通过chrome请求动态网页
    def process_request(self, request, spider):
        if spider.name == "zhihuSelenium":
            # self.browser = webdriver.Chrome(executable_path="D:/Package/chromedriver.exe")
            self.browser.get(request.url)
            time.sleep(1)
            print("访问:{0}".format(request.url))
            # browser.quit()
            return HtmlResponse(url=self.browser.current_url, body=self.browser.page_source,
                                encoding="utf-8", request=request)


