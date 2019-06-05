# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 11:46:03 2018

@author: Administrator
"""

import csv

# rows =  [{'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3',
#         'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3',
#         'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3',
#         'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3',
#         'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'}[]
#
# fieldnames = ['Column1','Column2','Column3','Column4'] #定义表头字段
# file = open('data11.csv', 'w')
# cr = csv.DictWriter(file, fieldnames = fieldnames)
# cr.writeheader() #将表头名称写入csv文件
# cr.writerows(rows) #将要写入的数据一次性写入到文件,也可以使用cr.writerow()一次写入一行