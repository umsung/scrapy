import itertools

natuals = itertools.count(1)

a = itertools.takewhile(lambda x: x<20, natuals)
print(list(a))

def pi(N):
    s = 0
    a = [i for i in range(2*N) if i%2==1]
    # print(a)
    for k,v in enumerate(a):
        if k%2 == 1:
            result=-4/v
        if k%2 == 0:
            result = 4/v
        s+=result
    return s

def pi2(N):
    jishu = itertools.count(1,2)
    a = itertools.takewhile(lambda x: x<=2*N-1, jishu)
    result = [4/v*(-1)**k for k,v in enumerate(a)]
    return sum(result)

print(pi2(10))

print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')