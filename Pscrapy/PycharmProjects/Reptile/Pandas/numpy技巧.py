# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 18:42:34 2019

@author: iHJX_Alienware
"""


'''
1、Numpy基础数据结构
NumPy数组是一个多维数组对象，称为ndarray。其由两部分组成：
① 实际的数据
② 描述这些数据的元数据

数组的基本属性
① 数组的维数称为秩（rank），一维数组的秩为1，二维数组的秩为2，以此类推
② 在NumPy中，每一个线性的数组称为是一个轴（axes），秩其实是描述轴的数量：
比如说，二维数组相当于是两个一维数组，其中第一个一维数组中每个元素又是一个一维数组
#以一维数组就是NumPy中的轴（axes），第一个轴相当于是底层数组，第二个轴是底层数组里的数组。
而轴的数量——秩，就是数组的维数。 
'''
import numpy as np

ar = np.array([1,2,3,4,5,6,7])
print(ar)          # 输出数组，注意数组的格式：中括号，元素之间没有逗号（和列表区分）
print(ar.ndim)     # 输出数组维度的个数（轴数），或者说“秩”，维度的数量也称rank
print(ar.shape)    # 数组的维度，对于n行m列的数组，shape为（n，m）
print(ar.size)     # 数组的元素总数，对于n行m列的数组，元素总数为n*m
print(ar.dtype)    # 数组中元素的类型，类似type()（注意了，type()是函数，.dtype是方法）
print(ar.itemsize) # 数组中每个元素的字节大小，int32l类型字节为4，float64的字节为8
print(ar.data)     # 包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。
ar   # 交互方式下输出，会有array(数组)


# 创建数组：array()函数，括号内可以是列表、元祖、数组、生成器等
ar1 = np.array(range(10))   # 整型
ar2 = np.array([1,2,3.14,4,5])   # 浮点型
ar3 = np.array([[1,2,3],('a','b','c')])   # 二维数组：嵌套序列（列表，元祖均可）
ar4 = np.array([[1,2,3],('a','b','c','d')])   # 注意嵌套序列数量不一会怎么样
print(ar1,type(ar1),ar1.dtype)


# 创建数组：arange()，类似range()，在给定间隔内返回均匀间隔的值。
print(np.arange(10))    # 返回0-9，整型
print(np.arange(10.0))  # 返回0.0-9.0，浮点型
print(np.arange(5,12))  # 返回5-11


# 创建数组：linspace():返回在间隔[开始，停止]上计算的num个均匀间隔的样本。
ar1 = np.linspace(2.0, 3.0, num=5)
ar2 = np.linspace(2.0, 3.0, num=5, endpoint=False)
ar3 = np.linspace(2.0, 3.0, num=5, retstep=True)
print(ar1,type(ar1))


# 创建数组：zeros()/zeros_like()/ones()/ones_like()
ar1 = np.zeros(5)  
ar2 = np.zeros((2,2), dtype = np.int)
ar3 = np.array([list(range(5)),list(range(5,10))])
ar4 = np.zeros_like(ar3)


# 数组类型转换：.astype()
ar1 = np.arange(10,dtype=float)
ar2 = ar1.astype(np.int32)
    # 注意：养成好习惯，数组类型用np.int32，而不是直接int32


# 基本索引及切片
ar = np.arange(20)
print(ar)
print(ar[4])
print(ar[3:6])
print('-----')
    # 一维数组索引及切片

ar = np.arange(16).reshape(4,4)
print(ar, '数组轴数为%i' %ar.ndim)   # 4*4的数组
print(ar[2],  '数组轴数为%i' %ar[2].ndim)  # 切片为下一维度的一个元素，所以是一维数组
print(ar[2][1]) # 二次索引，得到一维数组中的一个值
print(ar[1:3],  '数组轴数为%i' %ar[1:3].ndim)  # 切片为两个一维数组组成的二维数组
print(ar[2,2])  # 切片数组中的第三行第三列 → 10
print(ar[:2,1:])  # 切片数组中的1,2行、2,3,4列 → 二维数组
print('-----')
    # 二维数组索引及切片


'''
2、Numpy随机数
Numpy.random包含多种概率分布的随机样本，是数据分析辅助的重点工具之一
'''
import matplotlib.pyplot as plt 

# 随机数生成
samples = np.random.normal(size=(4,4))
print(samples)
    # 生成一个标准正太分布的4*4样本值

    
# 生成1000个均匀分布的样本值
a = np.random.rand()
    # 生成一个随机浮点数
b = np.random.rand(4)
    # 生成形状为4的一维数组
c = np.random.rand(2,3)
    # 生成形状为2*3的二维数组，注意这里不是((2,3))
samples1 = np.random.rand(1000)
samples2 = np.random.rand(1000)
plt.scatter(samples1,samples2)


# 生成1000个正太的样本值
samples1 = np.random.randn(1000)
samples2 = np.random.randn(1000)
plt.scatter(samples1,samples2)



















