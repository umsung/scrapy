import pandas as pd
import numpy as np


df_org = pd.read_excel('十二星座运势数据（源数据）.xlsx', sheet_name=0)
df = df_org.copy()
print(df['标题'].head())
print('iloc[1]:', df.loc[1])
df.dropna(inplace=True)  # inplace=True直接修改元数据上 或者 df = df.dropna()
df.rename(columns={'字段6': '商谈指数', '字段7':'幸运颜色', '字段8': '幸运数字', '字段9': '速配星座', '字段10': '短评', '标题': '星座'}, inplace=True)
print(df.columns)


def delword(data, *cols):
    for col in cols:
        data[col] = data[col].str.split('：').str[1]
    return data

df = delword(df, '商谈指数', '幸运颜色', '幸运数字', '速配星座', '短评')
df['商谈指数'] = df['商谈指数'].str.replace('%','')

print(df['商谈指数'].head())

def typefix(data, *cols):
    for col in cols:
        data[col] = data[col].astype(np.float)*0.01
    return data

df = typefix(df, '商谈指数')


def starfix(data, old, new):
    data = data.replace(old, new, regex=True)
    return data

dict = {'80px': '5', '64px': '4', '48px': '3', '32px': '2', '16px': '1'}
for d in dict:
    df = starfix(df, d, dict[d])

df['运势综合水平'] = (df['综合运势'].astype(np.float)+df['爱情运势'].astype(np.float)+df['事业学业'].astype(np.float)+df['财富运势'].astype(np.float))/4
print(df['运势综合水平'].head())

df['星座'] = df['星座'].str[:3]

df.rename(columns={'星座': 'org星座'}, inplace=True)

df_m = pd.read_excel('星座属性查询表.xlsx')

df = pd.merge(df, df_m, left_on='org星座', right_on='星座')

print(df.columns)
print(df[['星座', '属性']].head())

print(df['星座'].value_counts().index.tolist())
print(df['星座'].drop_duplicates().tolist())

# # pyecharts出图表
# import pyecharts as pe
# def figcreate_xz(df,name):
#     data_i = df[df['星座']==name][['运势综合水平','时间']].sort_values(by = '时间')
#     data_i.index = data_i['时间']
#     line.add(name,data_i.index.tolist(),data_i['运势综合水平'].tolist(),
#              yaxis_min = 2,
#              is_smooth=True,
#              is_datazoom_show=True)
#     # 创建函数，绘制图表
#
# line = pe.Line('不同星座运势图',width = 1500,height = 800)
# namelst = df['星座'].value_counts().index.tolist()
# for namei in namelst:
#     figcreate_xz(df,namei)
# line.render()
#     # 绘制不同星座运势图