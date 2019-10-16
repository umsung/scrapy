# 被装修的函数带参数
def func1(func):
    def add_func(a,b):
        print(a,b)
        a = 1
        b = 2
        print(func.__name__)
        return func(a,b)
    return add_func

@func1
def func2(x,y):
    print(x+y)

func2(10,20)
print(func2.__name__)