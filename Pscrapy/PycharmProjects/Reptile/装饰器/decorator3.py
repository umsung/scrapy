# 装饰器函数带参数
def arg_func(arg):
    def func1(func):
        def add_func():
            if arg == 'aaa':
                print('aaa')
            if arg == 'bbb':
                print('bbb')
            return func()
        return add_func
    return func1

@arg_func('aaa')
def test():
    print('is aaa')

test()