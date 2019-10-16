# __len()__
# __slots()__

# __str__ 打印出来的实例

class Student(object):
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__

# __iter__  一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

# __getattr__ 调用类的方法或属性时，如果不存在，就会报错,要避免这个错误,是写一个__getattr__()方法,动态返回一个属性

class Student2(object):
    def __init__(self):
        self.name = 'duan'

    def __getattr__(self,attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('Stundet2 object has no attrbute %s' % attr)


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

# __call__  定义一个__call__()方法，就可以直接对实例进行调用

class Student3(object):
    def __init__(self,name):
        self.name = name
    
    def __call__(self):
        print('定义__call__直接调用实例对象 %s' % self.name)


if __name__ == "__main__":
    s = Student2('duan')
    s()