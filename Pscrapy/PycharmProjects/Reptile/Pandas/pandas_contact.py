import pandas as pd

df = pd.read_excel('D:/l.xlsx', sheel_name=0)
print(df[df['代表'] != '[]'].head())

df1 = pd.read_csv('D:/people.csv')
print(df1.head())