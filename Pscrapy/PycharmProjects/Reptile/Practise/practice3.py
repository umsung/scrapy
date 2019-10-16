# 推导列表

print([x/2 for x in range(10) if x%2==0])

print([x for x in range(10) if x%2==0 and x%6==0])

print([x+1 if x>5 else x*2 for x in range(10)])

list_of_list = [[1,2,3],[4,5,6],[7,8,9]]
a=[]
def fun(list_of_list):
    for i in list_of_list:
        if isinstance(i,list):
            fun(i)
        else:
            a.append(i)

print([i for x in list_of_list for i in x])