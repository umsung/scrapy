import redis
import random
from config import *

class RedisClient(object):
    def __init__(self, host=HOST, port=PORT, password=PASSWORD):
        if password:
            db = redis.Redis(password=password,host=host,port=port)
        else:
            db = redis.Redis(host=host,port=port)
        self._db = db
        self.domain = ''
        self.name = ''

    def _key(self,key):
        '''
        返回格式化的key
        '''
        return '{domain}:{name}:{key}'.format(domain=self.domain,name=self.name,key=key)

    def keys(self):
        '''
        返回所有的格式化的key
        self._db.keys() 获取所有key
        self._db.keys('patter')  获取所有符合规则的key
        '''
        return self._db.keys('{domain}:{name}:*'.format(domain=self.domain,name=self.name))

    def get(self,key):
        '''
        根据键key获取值value
        '''
        raise NotImplementedError

    def set(self,key,value):
        '''
        设置键值对
        '''
        raise NotImplementedError

    def delete(self,key):
        raise NotImplementedError

    def flush(self):
        self._db.flushall()

   
class CookiesRedisClient(RedisClient):
    def __init__(self,host=HOST,port=PORT,password=PASSWORD,domain='cookies',name='default'):
        RedisClient.__init__(self,host,port,password)
        self.domain = domain
        self.name = name

    def get(self,key):
        '''
        根据键key获取值value
        '''
        try:
            return self._db.get(self._key(key)).decode('utf-8')
        except:
            print('GetCookiesError')
            return None

    def set(self,key,value):
        '''
        设置键值对
      
        '''
        try:
            self._db.set(self._key(key),value)
        except:
            print('SetCookiesError')
            return None

    def delete(self,key):
        try:
            self._db.delete(self._key(key))
        except:
            print('DeleteCookiesError')
            return None

    def random(self):
        try:
            keys = self.keys()
            return self._db.get(random.choice(keys))
        except:
            return None


    def count(self):
        return len(self.keys())

    def all(self):
        for key in self.keys():
            item = key.split(':').strip()
            if len(item) == 3:
                username = item[2]
                cookies = self.get(username)
                yield {
                    'username': username,
                    'cookies': cookies
                }


   
class AccountRedisClient(RedisClient):
    def __init__(self,host=HOST,port=PORT,password=PASSWORD,domain='account',name='default'):
        RedisClient.__init__(self,host,port,password)
        self.domain = domain
        self.name = name

    def get(self,key):
        '''
        根据键key获取值value
        '''
        try:
            return self._db.get(self._key(key))
        except:
            print('GetCookiesError')
            return None

    def set(self,key,value):
        '''
        设置键值对
        '''
        try:
            self._db.set(self._key(key),value)
        except:
            print('SetCookiesError')
            

    def delete(self,key):
        try:
            self._db.delete(self._key(key))
        except:
            print('DeleteCookiesError')
            return None

    def random(self):
        try:
            keys = self.keys()
            return self._db.get(random.choice(keys))
        except:
            return None


    def count(self):
        return len(self.keys())

    def all(self):
        for key in self.keys():
            item = key.split(':').strip()
            if len(item) == 3:
                username = item[2]
                password = self.get(username)
                yield {
                    'username': username,
                    'password': password
                }
