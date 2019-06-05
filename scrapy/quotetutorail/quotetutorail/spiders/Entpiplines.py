# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 企业信息爬虫管道
from openpyxl import Workbook
import pandas as pd
import numpy as np

class EntPipline(object):
    def __init__(self):
        # 创建excel，填写表头
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['名称', '地址','电话'])  # 设置表头

    def process_item(self,item,spider):

        for i in range(len(item["name"])):
            line = [(item['name'][i]), (item['address'][i]), (item['tel'][i]).replace('电话：', "")]
            self.ws.append(line)
            self.wb.save("F:\\"+spider.city+'-'+spider.keyword+".xlsx")
            # 读取Excel中Sheet1中的数据
            data = pd.read_excel("F:\\"+spider.city+'-'+spider.keyword+".xlsx")

            # 查看基于[名称]列去除重复行的数据
            wp = data.drop_duplicates(['名称', "地址", "电话"])

################################过滤非关键词#############################################
            #企业关键词
            if spider.keyword == '文化产业有限公司':
                bool = data['名称'].str.contains('文化产业.*?公司')
                filter_data = data[bool]
            if spider.keyword == "视觉艺术交流有限公司":
                bool = data['名称'].str.contains('视觉.*?艺术.*?公司')
                filter_data = data[bool]
            if spider.keyword == '动漫设计股份有限公司':
                bool = data['名称'].str.contains('动漫.*?公司')
                filter_data = data[bool]
            if spider.keyword == '互动娱乐有限公司':
                bool = data['名称'].str.contains('娱乐.*?公司')
                filter_data = data[bool]
            if spider.keyword == '国际展览有限公司':
                bool = data['名称'].str.contains('展览.*?公司')
                filter_data = data[bool]
            if spider.keyword == '网络股份有限公司':
                bool = data['名称'].str.contains('网络.*?股份.*?公司')
                filter_data = data[bool]
            if spider.keyword == "科技且孵化器有限公司":
                bool = data['名称'].str.contains('科技.*?孵化器.*?公司')
                filter_data = data[bool]
            if spider.keyword == '信息科技有限公司':
                bool = data['名称'].str.contains('信息.*?公司')
                filter_data = data[bool]
            if spider.keyword == '影视科技有限公司':
                bool = data['名称'].str.contains('影视.*?公司')
                filter_data = data[bool]
            if spider.keyword == '科技有限公司':
                bool = data['名称'].str.contains('科技.*?公司')
                filter_data = data[bool]
            if spider.keyword == '广告有限公司':
                bool = data['名称'].str.contains('广告.*?公司')
                filter_data = data[bool]
            if spider.keyword == "网络科技有限公司":
                bool = data['名称'].str.contains('网络.*?科技.*?公司')
                filter_data = data[bool]
            if spider.keyword == '游戏科技股份有限公司':
                bool = data['名称'].str.contains('游戏.*?公司')
                filter_data = data[bool]
            if spider.keyword == '新能源科技有限公司':
                bool = data['名称'].str.contains('新能源.*?公司')
                filter_data = data[bool]
            if spider.keyword == '文化传播有限公司':
                bool = data['名称'].str.contains('文化传播.*?公司')
                filter_data = data[bool]
            if spider.keyword == '动画制作有限公司':
                bool = data['名称'].str.contains('动画.*?公司')
                filter_data = data[bool]
            if spider.keyword == "教育科技有限公司":
                bool = data['名称'].str.contains('教育.*?公司')
                filter_data = data[bool]
            if spider.keyword == '创意科技股份有限公司':
                bool = data['名称'].str.contains('创意.*?科技.*?公司')
                filter_data = data[bool]
            if spider.keyword == '文化传媒有限公司':
                bool = data['名称'].str.contains('文化传媒.*?公司')
                filter_data = data[bool]
            if spider.keyword == '电子商务有限公司':
                bool = data['名称'].str.contains('电子商务.*?公司')
                filter_data = data[bool]
            if spider.keyword == "管理有限责任公司":
                bool = data['名称'].str.contains('管理.*?公司')
                filter_data = data[bool]

            #园区关键词
            if spider.keyword == '小镇产业园':
                bool = data['名称'].str.contains('小镇.*?产业园')
                filter_data = data[bool]
            if spider.keyword == '国际传媒产业园':
                bool = data['名称'].str.contains('国际传媒.*?产业园')
                filter_data = data[bool]
            if spider.keyword == '青年文创园':
                bool = data['名称'].str.contains('青年.*?文创园')
                filter_data = data[bool]
            if spider.keyword == '文化创意产业园区':
                bool = data['名称'].str.contains('文化创意.*?产业园')
                filter_data = data[bool]
            if spider.keyword == '动漫游戏产业园区':
                bool = data['名称'].str.contains('动漫.*?游戏.*?产业园')
                filter_data = data[bool]
            if spider.keyword == '工业园区':
                bool = data['名称'].str.contains('工业.*?园区')
                filter_data = data[bool]
            if spider.keyword == '科技产业园区':
                bool = data['名称'].str.contains('科教.*?产业园区')
                filter_data = data[bool]
            if spider.keyword == '游戏动漫产业园':
                bool = data['名称'].str.contains('游戏.*?动漫.*?产业园')
                filter_data = data[bool]

            #协会关键词
            if spider.keyword == '新媒体协会':
                bool = data['名称'].str.contains('新媒体.*?协会')
                filter_data = data[bool]
            if spider.keyword == '摄影家协会':
                bool = data['名称'].str.contains('摄影家.*?协会')
                filter_data = data[bool]
            if spider.keyword == '动画协会':
                bool = data['名称'].str.contains('动画.*?协会')
                filter_data = data[bool]
            if spider.keyword == '动漫产业协会':
                bool = data['名称'].str.contains('动漫.*?协会')
                filter_data = data[bool]
            if spider.keyword == '游戏产业协会':
                bool = data['名称'].str.contains('游戏.*?协会')
                filter_data = data[bool]

            # 将去除重复行的数据输出到excel表中
            filter_data.to_excel("F:\\"+spider.city+'-'+spider.keyword+".xlsx",index = False)

            return item

