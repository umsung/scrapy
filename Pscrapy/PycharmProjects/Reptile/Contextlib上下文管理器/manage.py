from contextlib import contextmanager
# 自定义一个上下文管理器，只需要定义一个类并且是实现__enter__()和__exit__()即可
# __enter__()：主要执行一些环境准备工作，同时返回一资源对象。如上下文管理器open("test.txt")的__enter__()函数返回一个文件对象。

# __exit__()：完整形式为__exit__(type, value, traceback),这三个参数和调用sys.exec_info()函数返回值是一样的，分别为异常类型、异常信息和堆栈。
# 装饰器contextmanager只需要写一个生成器函数就可以代替自定义的上下文管理器

@contextmanager
def open(filename, mode='r'):
    f = open(filename,'r')
    try:
        yield f
    finally:
        f.close()

@contextmanager
def locked(lock):

    lock.acquire()
    try:
        yield
    finally:
        lock.release()

@contextmanager
def transaction(db):
    db.begin()
    try：
        yield 
    except:
        db.rollback()
        raise
    else:
        db.commit()
  