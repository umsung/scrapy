# 装饰类的装饰器
# Python 对某个对象是否能通过装饰器（ @decorator）形式使用只有一个要求：decorator 必须是一个“可被调用（callable）的对象。
# 函数是callable对象，类实现了__call__方法就是callable对象

instances = {}

def singleton(cls):
    def get_instance(*args, **kw):
        cls_name = cls.__name__
        print(cls_name)
        print('===== 1 ====')
        if not cls_name in instances:
            print('===== 2 ====')
            instance = cls(*args, **kw)          
            instances[cls_name] = instance  # 把实例化对象User存入instace
            print(instance)
        return instances[cls_name]
    return get_instance

# 装饰器作用是限制只能有一个实例化对象，同时生成多个实例化对象，其实是同一个
@singleton
class User:
    _instance = None
    def __init__(self, name):
        print('===== 3 ====')
        self.name = name

u1= User('name')
u2= User('nam11e')
print(u1.name)
print(u2.name)