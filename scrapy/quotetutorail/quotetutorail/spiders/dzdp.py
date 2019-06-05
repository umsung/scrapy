# -*- coding: utf-8 -*-
import scrapy
import re
import json

class DzdpSpider(scrapy.Spider):
    name = 'dzdp'
    allowed_domains = ['dianping.com']
    start_urls = ['http://m.dianping.com/shenzhen/ch15/r8357']

    datas = []

    def start_requests(self):
        # for i in range(0, 59):
        #     self.datas.append(
        #         {
        #             'moduleInfoList': [{'moduleName': 'mapiSearch',
        #                                 'query':
        #                                     {'search':
        #                                         {
        #                                             'categoryId': '15',
        #                                             'cityId': '7',
        #                                             'keyword': '',
        #                                             'limit': '20',
        #                                             'locateCityid': '0',
        #                                             'maptype': '0',
        #                                             'parentCategoryId': '15',
        #                                             'regionId': '0',
        #                                             'sortId': '0',
        #                                             'start': str(i*20)}}}],
        #             'pageEnName': 'shopList'
        #         }
        #     )
        Payload = {
            'moduleInfoList': [{'moduleName': 'mapiSearch', 'query': {'search':
                                        {
                                            'categoryId': '15',
                                            'cityId': '7',
                                            'keyword': '',
                                            'limit': '20',
                                            'locateCityid': '0',
                                            'maptype': '0',
                                            'parentCategoryId': '15',
                                            'regionId': '0',
                                            'sortId': '0',
                                            'start': '20',
                                            'dpid': None,
                                            'pageModule': 'msiteshoplist'
                                        }
                            }}],
            'pageEnName': 'shopList',
        }

        # data = {'moduleInfoList': [{'moduleName': 'mapiSearch', 'query': {'search': {'categoryId': '15', 'cityId': '7', 'keyword': '', 'limit': '20', 'locateCityid': '0','maptype': '0', 'parentCategoryId': '15', 'regionId': '0', 'sortId': '0', 'start': '0', 'dpid': None, 'pageModule': 'msiteshoplist'}}

        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '234',
            'Content-Type': 'application/json',
            'Cookie': 's_ViewType=10; _lxsdk_cuid=167a12e4c4cc8-0c6bd3ec1714d7-546f3a7b-13c680-167a12e4c4dc8; _lxsdk=167a12e4c4cc8-0c6bd3ec1714d7-546f3a7b-13c680-167a12e4c4dc8; _hc.v=7c0c148c-3496-0230-0e2b-c80fa9b780ca.1544597425; cityid=7; logan_custom_report=; pvhistory=6L+U5ZuePjo8L2Vycm9yL2Vycm9yX3BhZ2U+OjwxNTQ0NTk4MjA3NTE2XV9b; m_flash2=1; default_ab=shop%3AA%3A1%7Cindex%3AA%3A1%7CshopList%3AA%3A1; msource=default; logan_session_token=slcx73holc8vw6jy95gj; _lxsdk_s=167a17f2e94-3f3-3d6-7b5%7C%7C1116',
            'Host': 'm.dianping.com',
            'Origin': 'http://m.dianping.com',
            'Referer': 'http://m.dianping.com/shenzhen/ch15',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
            # 'X-Requested-With': 'XMLHttpRequest',
        }
        request_url = 'http://m.dianping.com/isoapi/module'

        yield scrapy.Request(url=request_url, method="POST", headers=headers, body=json.dumps(Payload), callback=self.parse, dont_filter=True)


        # yield scrapy.Request(url=request_url, headers=headers, meta={'payloadFlag': True, 'payloadData': data, 'headers': headers}, callback=self.parse)

    def parse(self, response):
        print(response.text)
        results = json.loads(response.text)
        if results and 'data' in results.keys():
            node_list = dict(results.get('data').get('moduleInfoList')[0]).get('moduleData').get('data').get('listData').get('list')
            # print(node_list)
            if node_list:
                for node in node_list:
                    item = {}
                    item['name'] = node['name']
                    item['shopId'] = node['shopId']
                    item['priceText'] = node['priceText']
                    item['reviewCount'] = node['reviewCount']
                    item['matchText'] = node['matchText']
                    detail_url = 'http://m.dianping.com/shop/' + str(item['shopId'])
                    yield scrapy.Request(url=detail_url, callback=self.detail_parse, meta={'item': item})
        # if results and 'data' in results.keys():
        #     isEnd = results['data']['moduleInfoList']['moduleData']['data']['listData']['isEnd']
        #     startIndex = results['data']['moduleInfoList']['moduleData']['data']['listData']['startIndex']
        #     if startIndex and isEnd == 'false':
        #         url =
        #         yield scrapy.Request(url=startIndex, callback=self.parse)

    def detail_parse(self,  response):

         # address1 = re.search(r'<div class = "addressLogo"></div>.*?<span class= "addressText">.*?</span>(.*?)</span>', response.body.decode('utf-8'), re.S)
         # # address = address.group(1)
        item = response.meta['item']
        item['tel'] = re.search(r'<div class="aboutPhoneNum">.*?<a class="tel" href="(.*?)"', response.text, re.S).group(1)
        # # tel = re.sub('tel:', '', tel)
        item['address'] = re.search(r'<textarea style="display:none" id="shop-detail">.*?"address":"(.*?)"', response.body.decode('utf-8'), re.S).group(1)
        yield item


        # print(address, tel)
        # print(response.body.decode('utf-8'))





