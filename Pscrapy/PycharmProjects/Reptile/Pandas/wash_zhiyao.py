import pandas as pd
import numpy as np
import time
import re

def washZhiYao1():
    df = pd.read_excel('2000-4000.xlsx', encoding='gbk')
    # print(len(df['处方'].tolist()))   # 统计处方列的长度

    print(df[df['处方'].isnull().values == True]['ID'])   # 找出处方列为缺失值的行的url
    df = df.dropna(subset=['处方'])  # 删除处方列含有缺失值的行
    df['处方'] = df['处方'].str.replace('。','')
    df['处方'] = df['处方'].str.replace('\.$', '')
    # re.sub('\.$', '', df['处方'].str)
    df = df[~df['处方'].str.contains('（')]   # 选出不含有‘（’的列
    print(df['处方'].head(3))
    clists = df['处方'].str.split('，|、| |,').tolist()   # 根据'，'分割并转成列表
    print(clists)
    count = 1
    data_l = []
    for index, clist in enumerate(clists):
        url = df.iloc[index]['ID']
        for i in clist:

            if '1' in i or '2' in i or '3' in i or '4' in i or '5' in i or '6' in i or '7' in i or '8' in i or '9' in i or '0' in i:
                if '.' in i or '-' in i or '～' in i:
                    name = re.findall(r'(.*?)\d+.*?\d+', i, re.S)[0]
                    num = re.findall(r'(\d+.*?\d+)', i, re.S)[0]
                    unit = re.findall(r'.*?\d+.*?\d+(.*)', i, re.S)[0]
                    print(count, name, num, unit, url)
                elif len(re.findall('\d+', i)) >= 2 and '.' not in i:
                    name = re.findall(r'(.*?)\d+.*', i, re.S)[0]
                    num = re.findall(r'.*?(\d+.*)', i, re.S)[0]
                    unit = i[-1]
                    print(count, name, num, unit, url)
                else:
                    name = re.findall(r'(.*?)\d+.*?', i, re.S)[0]
                    num = re.findall(r'(\d+)', i, re.S)[0]
                    unit = re.findall(r'.*?\d+(.*)', i, re.S)[0]
                    print(count, name, num, unit, url)

            elif '半两' in i or '半钱' in i or '半支' in i:
                name = re.findall(r'(.*?)半', i, re.S)[0]
                num = '半'
                unit = re.findall(r'半(.*)', i, re.S)[0]
                print(count, name, num, unit, url)

            else:
                name = i
                num = ''
                unit = ''
                print(count, name, num, unit, url)

            count = count + 1
            data_l.append([name, num, unit, url])
    print(data_l)
    create_excel(data_l)


def washZhiYao2():
    df = pd.read_excel('2000-4000.xlsx', sheet_name=0)
    null_url = df[df['处方'].isnull().values == True]['ID']
    df = df.dropna(subset=['处方'])
    df.drop_duplicates()
    df = df[df['处方'].str.contains('（|）')]
    df['处方'] = df['处方'].str.replace('。', '')
    df['处方'] = df['处方'].str.replace('\.$', '')
    print(df['处方'].head(10))
    clists = df['处方'].str.split('，|、| ').tolist()
    print(clists)
    count = 1
    data_d = []
    for index, clist in enumerate(clists):
        url = df.iloc[index]['ID']
        for i in clist:
            if '1' in i or '2' in i or '3' in i or '4' in i or '5' in i or '6' in i or '7' in i or '8' in i or '9' in i or '0' in i:

                if '（' in i or '）' in i:
                    name = re.findall(r'(.*?)\（.*', i, re.S)
                    opera = re.findall(r'.*?(\（.*?)\d+', i, re.S)
                    num = re.findall(r'.*?(\d+).*', i, re.S)
                    unit = re.findall(r'.*?\d+(.*)', i, re.S)
                    print(count, name, opera, num, unit, url)
                else:
                    name = re.findall(r'(.*?)\d+.*?', i, re.S)
                    opera = ''
                    num = re.findall(r'(\d+)', i, re.S)
                    unit = re.findall(r'.*?\d+(.*)', i, re.S)
                    print(count, name, opera, num, unit, url)
                count = count+1
                data_d.append([name, opera, num, unit, url])
    create_excel(data_d)


def create_excel(data_l):
    df = pd.DataFrame(data_l, columns=['name', 'num', 'opera' 'unit', 'url'])
    df.to_excel('./zhiyao1.xlsx', encoding='utf-8', index=0)


if __name__ == '__main__':
    washZhiYao2()