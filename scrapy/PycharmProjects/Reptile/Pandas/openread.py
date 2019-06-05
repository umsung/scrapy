##加载前加上这几行
# -*- coding : utf-8 -*-
# coding: utf-8

# 加载时，设置编码格式为encoding="gbk"

# f = open('C:/scrapy/PycharmProjects/Reptile/Pandas/01.xlsx', 'r', encoding='gbk')
# for i in f.readlines()[:5]:
#     print(i.encode('utf-8'))

import pandas as pd
import numpy as np

df = pd.read_excel('tt.xlsx', sheet_name=0, header=None, names = ['电话', '地址', '公司'])
df['省会'] = df['地址'].str.split('.').str[0]
df['城市'] = df['地址'].str.split('.').str[1]
df['详细地址'] = df['地址'].str.split('.').str[2]
df['电话'] = df['电话'].str.split('：').str[1]

# 去重
df.drop_duplicates()

# 删除指定行、列
# df.drop('地址', axis=1) # 删除指定列
# df.drop(['1', '2']) # 删除指定行
# del df['地址']  # 删除指定列

# 删除含有空值的行或列 df.dropna()  返回删除后的表
# print(df.dropna())  # 默认删除行，有空值的行就删除
# print(df.dropna(axis=1))  # 删除列，有空值的列就删除
# print(df.dropna(how='all'))  # 所有值全为缺失值的行才删除
# print(df.dropna(thresh=2)) # "至少出现过两个缺失值才删除"
# print(df.dropna(subset=['电话', '城市']))  # "返回删除这个subset中的含有缺失值的行或列的df表"

# 填充缺失值和替代空值fillna。（空值是” “， 缺失值是NAN）
df['公司'] = df['公司'].fillna('缺失项').head(10)
print(df['公司'].head(10).tolist())
df['公司'][df['公司'] == ''] = '测试'

print(df.dropna()['公司'].head(10))
print(df['公司'].head(10))

# df['公司'] = df['公司'].str.strip()  # 去除电话一列中数据中间的空格
# print(df['公司'].head(10))


df1 = df[(df['电话'].str.contains('暂无')) & (df['城市'] != '东城区')]  # 筛选指定数据
print(df1.head(10).loc[[1,16,10]])
# df1.to_excel('11.xlsx') 生成清洗后的excel