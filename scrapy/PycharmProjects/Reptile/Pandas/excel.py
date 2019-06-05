import pandas as pd
import numpy as np
from pandas import Series, DataFrame


def read_csv():
    # sheet_name指定表。默认是sheet_name=0，sheetname=None是返回全表
    # header指定作为列名的行，默认0；若数据不含列名，则设定 header = None；
    # skiprows：省略指定行数的数据, 自上而下的开始略去数据的行, skip_footer：省略从尾部数的行数据
    # index_col ：指定列为索引列, 从0开始
    # names：指定列的名字，传入一个list数据
    # encoding='gbk'转码
    df = pd.read_excel('贵阳-视觉艺术01.xlsx', sheet_name=0, header=None, skiprows=2, names=['名称', '地址', '电话'])
    # print(df.head())
    df1 = df[~ df['电话'].str.contains('暂无')]
    # print(df1.head())

    # 筛选分割
    df1['省分'] = df1['地址'].str.split('.').str[0]
    df1['城市'] = df1['地址'].str.split('.').str[1]
    df1['详细地址'] = df1['地址'].str.split('.').str[2]
    del df1['地址']

    # 返回去除重复行的数据
    df1.drop_duplicates()  # 返回去除重复行的数据
    # df1[df1.duplicated() == False]

    # 返回头5条数据  df.head()
    print(df1[['电话', '详细地址']].head())
    print(df1.groupby('城市'))
    # df1.to_excel('清洗.xlsx', index=False)

    # 分组 df.groupby
    # df1.groupby('城市')['地址'].count()

    # 合并 df.merge

    # # 筛选包含指定数据的列
    # bool = data['名称'].str.contains('视觉.*?艺术')
    # bool2 = data['地址'].str.contains('贵阳市')
    # bool3 = ~data['电话'].str.contains('暂无')
    # filter_data = data[bool & bool2 & bool3]
    #
    # print(filter_data)

    # print(data)
    # 查看是否有重复行
    # re_row = data.duplicated()
    # print(re_row)
    #
    # 返回去除重复行的数据
    # print(data['名字'])

    # no_re_row = data.drop_duplicates()
    # print(no_re_row)
    #

    # # 返回基于指定字段去除重复行的数据
    # wp = data.drop_duplicates(['名字', '地址', '电话'])

    # 将去重数据输入到excel
    # no_re_row.to_excel('D://12.xls', index=False, encoding='gbk')


if __name__ == '__main__':
    read_csv()