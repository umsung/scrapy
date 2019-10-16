import functools

def log(arg=''):
    def decorator(func):
        @functools.wraps(func)
        def warpper(*args, **kw):
            print('%s begin call %s' %(func.__name__, arg))
            result = func(*args, **kw)
            print('%s end call %s' %(func.__name__, arg))
            print('result:', result)
            return result
        return warpper
    return decorator

@log()
def test1():
    print('111')

@log('log')
def test2():
    print('222')


test1()
test2()