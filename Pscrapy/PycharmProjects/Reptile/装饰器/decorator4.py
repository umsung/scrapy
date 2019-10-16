# 装饰器作用于任意函数
import time
import functools

# 需要把原始函数的__name__等属性复制到wrapper()函数中,经过decorator装饰之后的函数，
# 它们的__name__已经从原来的'now'变成了'wrapper'

# functools .wraps 装饰器，它的作用就是将 被修饰的函数的一些属性值赋值给 修饰器函数

def func1(func):
    @functools.wraps(func)
    def add_func(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        end_time = time.time()
        print('%s excute use time is %s ms' %(func.__name__, end_time-start_time))
        return result
    return add_func


@func1
def test1(x,y):
    print(x+y)
    return x+y


@func1
def test2(x,y,z):
    print(x*y*z)
    return x*y*z
print(test1.__name__)
a = test1(10,20)
b = test2(1,2,3)
if a != 30:
    print('fail')
elif b != 6:
    print('fail')
else:
    print('success')
