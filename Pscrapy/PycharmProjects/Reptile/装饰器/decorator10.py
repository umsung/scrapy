import functools


class logger(object):
    def __init__(self,duation,func):
        self.duation = duation
        self.func = func

    def __call__(self,*args, **kw):
    
        print('wait %s S' % self.duation)
        return self.func(*args, **kw)
    


def pianfunc(duation=2):
    return functools.partial(logger, duation)

@pianfunc()
def dec(x,y):
    print(x+y)


dec(1,2)


