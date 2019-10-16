import functools

def log(parm):
    if isinstance(parm, str):
        def decorator(func):
            @functools.wraps(func)
            def wapper(*args, **kw):
                print('%s,%s' %(parm, func.__name__))
                return func(*args, **kw)
            return wapper
        return decorator
    else:
        @functools.wraps(parm)
        def wapper(*args, **kw):
            print('%s' % parm.__name__)
            return parm(*args, **kw)
        return wapper


@log
def test1():
    print('111')


test1()
print(test1.__name__)