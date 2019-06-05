def debug(func):
    print('test1111')
    def wrapper(*args,**kwargs):
        print('test')
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper

@debug
def say_hello(parag):
    print("hello!", parag)


if __name__ == '__main__':
    say_hello("sadasdsa")
    # say_goodbye()