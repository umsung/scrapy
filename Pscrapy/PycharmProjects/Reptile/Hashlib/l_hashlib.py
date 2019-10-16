from hashlib import md5
import random,hmac

def hashlib_md5(password):
    return md5(password.encode('utf-8')).hexdigest()

def hmac_md5(key,s):
    return hmac.new(key.encode('utf-8'),s.encode('utf-8'),'md5')

class User(object):
    def __init__(self, user, password):
        self.user = user
        self.salt = ''.join([chr(random.randint(48,122)) for i in range(20)])
        self.password = hashlib_md5(password+self.salt)


class User2(object):
    def __init__(self, user, password):
        self.user = user
        self.salt = ''.join([chr(random.randint(48,122)) for i in range(20)])
        self.password = hmac_md5(self.salt,password)


db = {
    'michael': User('duan','111111'),
    'bob': User('duan','123456'),
    'alice': User('duan','888888')
}

db2 = {
    'michael': User('duan','111111'),
    'bob': User('duan','123456'),
    'alice': User('duan','888888')
}

def login(username,password):
    user = db[username]
    return user.password == hashlib_md5(password+user.salt)

def login2(username,password):
    user = db2[username]
    return user.password == hmac_md5(user.salt,password)

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')