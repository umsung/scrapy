# -*- coding:utf-8 -*-
import datetime
from datetime import timedelta

today = datetime.datetime.now()

a = ['今天', '昨天', '明天', '前天', '1分钟前', '1小时前', '1天前', '1月前', '1年前']
for i in a:
    date = ''
    if '今天' in str(i):
        date = str(today).split(' ')[0]
    elif '昨天' in str(i):
        tim = today - timedelta(days=int(1))
        date = str(tim).split(' ')[0]
    elif '前天' in str(i):
        tim = today - timedelta(days=int(2))
        date = str(tim).split(' ')[0]
    elif '明天' in str(i):
        tim = today + timedelta(days=int(1))
        date = str(tim).split(' ')[0]
    elif '分钟前' in str(i):
        minutes = str(i).replace("分钟前", "").strip()
        date = (today - timedelta(minutes=int(minutes))).strftime("%Y-%m-%d %H:%M:%S")
    elif '小时前' in str(i):
        hours = str(i).replace("小时前", "").strip()
        date = (today - timedelta(hours=int(hours))).strftime("%Y-%m-%d %H:%M:%S")
    elif '天前' in str(i):
        days = str(i).replace("天前", "").strip()
        tim = today - timedelta(days=int(days))
        date = str(tim).split('.')[0]
    elif '月前' in str(i):
        days = str(i).replace("月前", "").strip()
        date = (today - timedelta(days=int(days) * 30)).strftime("%Y-%m-%d %H:%M:%S")
    elif '年前' in str(i):
        days = str(i).replace("年前", "").strip()
        date = (today - timedelta(days=int(days) * 365)).strftime("%Y-%m-%d %H:%M:%S")
    else:
        date = str(i)
    print('%s：%s' % (i, date))
