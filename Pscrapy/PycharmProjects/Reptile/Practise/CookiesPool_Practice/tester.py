from db import *
from config import *
import requests
import json
import lxml
from lxml import etree

class Tester(object):
    def __init__(self, name):
        self.name = name
        self.cookies_db = CookiesRedisClient(name=self.name)
        self.account_db = AccountRedisClient(name=self.name)

    def test(self,account,cookies):
        raise NotImplementedError

    def run(self):
        cookies = self.cookies_db.all()
        for i in cookies:
            cookie = i['cookies']
            account = i['username']
            self.test(cookie,account)

class TestValidCookie(Tester):
    def __init__(self, name):
        Tester.__init__(self,name)
        self.name = name

    def test(self,account,cookie):
        print('test acount %s' %account)
        try:
            cookie = json.dumps(cookie)
        except TypeError:
            print('Invalid cookies')
            self.cookies_db.delete(account)
            print('delete Invalid cookies %s' %account)

        try:
            resp = requests.get('http://weibo.cn', cookies=cookie)
            if resp.status_code == 200:
                selector = etree.HTML(resp.text)
                title = selector.xpath('title')[0]
                if '' in title:
                    print('Valid Cookies', cookie)
                else:
                    print('Invalid cookies', cookie)
                    self.cookies_db.delete(account)
                    print('delete Invalid cookies %s' %cookie)
        except ConnectionError:
            print('Invalid cookies', cookie)
            self.cookies_db.delete(account)
            print('delete Invalid cookies %s' %cookie)