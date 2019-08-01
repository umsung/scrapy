import pandas as pd
import numpy as np
from pandas import Series, DataFrame


# name = ['one', 'two', 'three', 'four', 'five']
# df = pd.read_excel('C:/Users/Administrator/Desktop/ss.xlsx', nrows=10)
# print(df)
def starfix(data, old, new):
    data = data.replace(old, new, regex=True)
    return data


df1 = DataFrame({'keys': ['a', 'b', 'c', 'd', 0, 8], 'data': range(6)})
print(df1)
print(df1.loc[1])
print(df1.iloc[1])
print(df1.index)
print(df1.columns)

df1 = df1.replace(0, 99)
print(df1)

dict = {'a': 'templetpate', 1: '11', 3: '33'}
for i in dict:
    df1 = starfix(df1, i, dict[i])
print(df1)
#
# df2 = DataFrame({'keys': ['a', 'f', 'g', 'd'], 'data1': range(4)})
# print(df2)
#
# a = pd.merge(df1, df2, on='keys', how='left')
# b = pd.concat([df1, df2], sort=True)
# print(a)
# print(b)