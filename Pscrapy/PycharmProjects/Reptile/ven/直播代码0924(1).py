# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 20:02:07 2019

@author: iHJX_Alienware
"""

import pymongo
    # 导入工具包

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    # ① 连接数据库

db1 = myclient['拉勾网']
db2 = myclient['链家']
    # ② 读取数据库，拉勾网，链家

table1 = db1['拉勾网数据采集（1）']
    # ③ 读取数据库中的集合
    # sql里table，mongo是集合
    
    
# 查询单条数据
table1.find_one()

# 查询所有数据
table1.find({})
    # 结果是一个pymongo的对象
list(table1.find({}))    
    
    
'''
创建1个新的数据库，存储5条数据
'''
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    # ① 连接数据库
db3 = myclient['直播0924']
    # 创建数据库
    # 当数据库存在的时候，读取数据库
    # 当数据库不存在的时候，创建数据库
    # 如果创建数据库，必须存入数据，才能真正的创建
table3 = db3['测试集合']
    # 创建集合
data1 = {'age': 19, 'name': 'jack'}
data2 = {'gender': 'male', 'name': 'hh'}

table3.insert_one(data1)
table3.insert_one(data2)
    # 数据入库
    
    
'''
如何从mongo中读取数据
'''
# ① 先从mongo读取
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db4 = myclient['链家']
table4 = db4['data01']
datalst = list(table4.find({}))
    #实现了读取，并存入1个列表

# 借助pandas来将数据处理成 表格的样子
import pandas as pd
data = pd.DataFrame(datalst)

# 数据导出excel
data.to_csv('C:/Users/iHJX_Alienware/Desktop/s.csv')


'''
如何将数据导入mongo
'''
data2 = pd.read_csv('C:/Users/iHJX_Alienware/Desktop/s.csv',encoding='gbk')
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db4 = myclient['直播0924']
table4 = db4['链家数据导入']
    #实现了读取，并存入1个列表
datalst2 = data2.to_dict(orient='records')
table4.insert_many(datalst2)  
    
    
'''
假如你的数据入库了，用sql和用mongo的区别
data02_new 查询“价格_万”字段，大于300万的房源数据的
“小区名称”和“户型”字段
'''
# SQL语句
# SELECT 小区,户型 FROM data02_new WHERE 价格_万 >300;

# mongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db4 = myclient['链家']
table4 = db4['data02_new']

datalst3 = list(table4.find({}))
data3 = pd.DataFrame(datalst3)

result = data3[data3['价格_万']>300][['小区','户型','价格_万','关注人数']]

import matplotlib.pyplot as plt
import matplotlib.style as psl
psl.use('ggplot')

   
plt.figure(figsize=(12,8))  
plt.scatter(result['价格_万'],result['关注人数'])    




























