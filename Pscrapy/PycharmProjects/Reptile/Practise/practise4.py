
num = input('输入数字：').strip()
num = int(num)
for i in range(1, num):
    
    print(' '*(num-i),'* '*i)
