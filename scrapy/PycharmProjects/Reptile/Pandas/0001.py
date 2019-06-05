#encoding:utf-8
import os, sys
import csv
import re
import time
from openpyxl import Workbook

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.rand(10,3), columns=['a','b','c'])
    # 创建数据
print(df.plot(kind='bar',grid = True,figsize = (12,8),colormap='Reds_r'))

lists = ['100-200人', '20-88人', '300000人', '201-400人', '99人', '101人']

for i in lists:
    a = re.findall(r'(.*?)人', i, re.S)[0]
    if '-' in a:
        a = a.split('-')[-1]
    if int(a) > 100:
        print(i)
    # else:
    #     if int(a) > 100:
    #         print(i)

# now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# fname = "D:/logs/" + now + r"report.xlsx"
# wb = Workbook()
# ws = wb.active
# ws.append(['1', '2', '3'])
# wb.save(fname)
# csvFile = open(fname, 'a')
# fileHeader = ["x", "y", "z"]
# writer = csv.writer(csvFile)
# writer.writerow(fileHeader)
#
#
# csvFile.close()