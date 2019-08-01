#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: xag
@license: Apache Licence
@contact: xinganguo@gmail.com
@site: http://www.xingag.top
@software: PyCharm
@file: Red_Wars.py
@time: 12/7/19 09:59
@description：抢红包
"""

# -*- encoding=utf8 -*-
__author__ = "xingag"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)




def get_red_package():
    # 3、获取群消息列表
    msg_list_elements_pre = poco('android.widget.ListView').children()
    a = []
    for i in msg_list_elements_pre:
        a.insert(0, i)
        print(len(a))

    for i in a:
        redelement  = i.offspring('com.tencent.mm:id/aq3')
        lingqu = i.offspring('com.tencent.mm:id/aq6')
        if redelement.exists():
            if lingqu.exists() and (lingqu.get_text() == '已被领完' or lingqu.get_text() == '已领取'):
                print('已被领取')
                continue
            else:
                redelement.click()
                kai = poco("com.tencent.mm:id/cy7").child('com.tencent.mm:id/cyf')
                if kai.exists():
                    print('可以领取')
                    kai.click()
                    keyevent('back')
        else:
            print('无')
            continue

if __name__ == '__main__':
    # 1、打开微信
    poco(text='微信').click()

    target = input('请输入名称：')

    # 2、获取微信列表
    item_elements = poco(name='com.tencent.mm:id/b5m').offspring('com.tencent.mm:id/b5o')

    names = list(map(lambda x: x.get_text(), item_elements))

    if target in names:
        index = names.index(target)
        item_elements[index].click()
        while True:
            start_time = time.time()
            get_red_package()
            end_time = time.time()
            sj = ('%.2f' % (end_time-start_time))
            print('sj', sj)
            time.sleep(2)
            print('继续')
    else:
        print('找不到输入的名称')



# 3、获取想要的信息