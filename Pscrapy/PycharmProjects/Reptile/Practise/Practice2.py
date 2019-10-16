'''杨辉三角
          1        
        1   1   
      1   2   1    
    1   3   3   1
  1   4   6   4   1
1   5   10  10  5   1

'''

def trigger():
    L=[1]
    while True:
        yield L
        L =[1] + [L[i]+L[i-1] for i in range(1,len(L))] + [1]

def trigger2():
    L=[1]
    while True:
        yield L
        L = [sum(i) for i in zip([0]+L,L+[0])]

n=1
result = []
for i in trigger2():
    result.append(i)
    
    n=n+1
    if n > 6:
        break
for i in result:
    print(i)