def func1(func):
    def add_func():
        print('新加的功能')
        # 在这里添加功能
        return func()
        # func 函数调用
        # func() 执行这个函数，返回函数的结果
    return add_func

@func1
def func2():
    print('原来的功能')
    # 原来的功能


func2()
# 等价于func1(func2())

# 装饰器的功能 是 在不改变 func2的前提下，给其添加更多功能