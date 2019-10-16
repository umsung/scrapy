
# 带参数和不带参数的类装饰器有很大的不同。
# 类装饰器一般是装饰函数
# __init__ ：不再接收被装饰函数，而是接收传入参数。
# __call__ ：接收被装饰函数，实现装饰逻辑。
# Python 对某个对象是否能通过装饰器（ @decorator）形式使用只有一个要求：decorator 必须是一个“可被调用（callable）的对象。
# 函数是callable对象，类实现了__call__方法就是callable对象

class logger(object):
    def __init__(self, level=''):
        self.level = level

    def __call__(self, func):
        def warppe(*args, **kw):
            print('[{level}]: the function {a}() is running..'.format(level=self.level,a=func.__name__))
            return func(*args, **kw)
        return warppe

@logger('WARNING')
def say(something):
    print('say {}!'.format(something))

say('hello')
print(say.__name__)