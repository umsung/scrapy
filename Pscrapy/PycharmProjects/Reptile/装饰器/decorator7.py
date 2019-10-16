# 类装饰器
# 不带参数
# 基于类装饰器的实现，必须实现 __call__ 和 __init__两个内置函数。
# __init__ ：接收被装饰函数
# __call__ ：实现装饰逻辑。

class logger(object):
    def __init__(self, func): # 接收装饰函数
        self.func = func

    def __call__(self,*args, **kw):
        print('[INFO]: the function {}() is running...'.format(self.func.__name__))
        return self.func(*args, **kw)
        
@logger  
def say(something):
    print('say {}!'.format(something))

say('hello')
