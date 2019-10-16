import requests
import re
from lxml import etree
import numpy as np
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Cookie': '__guid=169583271.388253713253878400.1534817461127.2454; _lxsdk_cuid=1655a3fe904ab-01904d5c1cf2fe-5d4e211f-100200-1655a3fe905c8; _lxsdk=1655a3fe904ab-01904d5c1cf2fe-5d4e211f-100200-1655a3fe905c8; _hc.v=44ef0c90-1a7b-d24c-1b86-87c1c2f6bd65.1534817463; s_ViewType=10; cy=10; cye=tianjin; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=1696aa54b17-4ec-56-0d2%7C%7C432', 'Host': 'www.dianping.com', 'If-Modified-Since': 'Sun, 10 Mar 2019 07', 'If-None-Match': '"555b6df9fea08164bb49fd7e966d99b3"', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
css_header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Host': 's3plus.meituan.net', 'If-Modified-Since': 'Wed, 06 Mar 2019 14', 'If-None-Match': '"4684b1c3dee8f4d172b2ac0c11e827a1"', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


def get_code(url):
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    selector = etree.HTML(response.text)
    nodelist = selector.xpath('//*[@class="expand-info tel"]')[0]
    item = etree.tostring(nodelist).decode('utf-8')
    print(item)
    item = re.sub('<span.*?</span>', '', item, re.S)
    items = re.findall('<d class="(.*?)">|(\d+)', item, re.S)
    #  [('', '1'), ('', '63504'), ('', '62468'), ('', '58623'), ('', '58973'), ('', '60461'), ('', '57988'), ('', '1'), ('', '58623'), ('', '57979'), ('', '57979')]

    phone_list = []
    print(items)
    for i in items:
        phone_list.append(i[0] if i[0] != '' else i[1])
        # if i[0] != '':
        #     phone_list.append(i[0])
        # else:
        #     phone_list.append(i[1])
    print(phone_list)
    return phone_list


#获取css的url
def get_css():
    response = requests.get('http://www.dianping.com/shop/97404408', headers=headers).text
    html = etree.HTML(response)
    css_url = html.xpath('//link[@rel="stylesheet"]/@href')
    # return 'http:' + css_url[1]
    css = requests.get('http:' + css_url[1], headers=css_header)
    css.encoding = 'utf-8'
    return css.text


#获取svg
def get_svg(css_text):
    res = re.search('.*?oul8fr', css_text, re.S)
    print(res)
    res = res.group(0)
    res = re.findall('url.*?\.svg', res, re.S)[-2]
    url = re.sub('url\(', 'http:', res)
    response = requests.get(url).content

    return response

# css_header={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Host': 's3plus.meituan.net', 'If-Modified-Since': 'Wed, 06 Mar 2019 14', 'If-None-Match': '"4684b1c3dee8f4d172b2ac0c11e827a1"', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
# css=requests.get(css_url,headers=css_header)
# css.encoding='utf-8'
# css.text


#用正则表达式获取background中对应的x和y
def get_x(code, css_text):
    return re.search(code+'{background:-(.*?)px -(.*?)px;}', css_text, re.S).groups()


# 根据svg，x,y来获取对应的数字，此函数可以继续优化，返回字典，直接传入x值
def get_num(svg, x_, y):
    html = etree.HTML(svg)
    # 获取所有的y值
    y_list = html.xpath('//text/@y')
    y_list = [int(y) for y in y_list]  # 数据类型转换
    y_list = np.array(y_list)  # 构造array
    y_list = y_list.astype(np.int64)  # 数据类型转换
    y_index = np.abs(y_list - y).argsort()[0]  # 计算距离y最近的index
    y_ = y_list[y_index]  # 获取到要取的y值
    x = html.xpath('//text[@y="{y}"]/@x'.format(y=y_))  # 获取到正确的x列表
    num = html.xpath('//text[@y="{y}"]/text()'.format(y=y_))  # 获取到对应的y的列表

    dict_x = dict(zip(x[0].split(), list(num[0])))  # 构造字典
    return dict_x[str(x_)]  # 返回正确的x值


def main():
    tel = []  # 用于保存最后生成的结果
    codes = get_code('http://www.dianping.com/shop/97404408')  # 获取code
    css_text = get_css()
    print(css_text)
    svg = get_svg(css_text)
    print(svg)
    for i in codes:
        if len(i) == 1:
            tel.append(i)  # 如果本身代表的是数字，则直接加到列表中
        else:
            i = i.replace('"', '')
            x, y = get_x(i, css_text)
            # 数字进行预处理
            x = int(float(x)) + 6
            y = int(float(y)) + 30
            # print(x,y)
            tel.append(get_num(svg, x, y))
    print(''.join(tel))  # 组成字符串


if __name__ == '__main__':
    url = 'http://www.dianping.com/shop/97404408'
    get_code(url)
    # main()


# tel=[]#用于保存最后生成的结果
# codes = get_code('http://www.dianping.com/shop/97404408')#获取code
# #举例，svg_url获取方式参考css中url的获取方式,后面有获取svg url的正则表达式
# svg_url = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/552560215a8c8f609b7fb7bd1664070d.svg'
#
# svg = get_svg(svg_url)
# for i in codes:
#     if len(i) == 1:
#         tel.append(i)#如果本身代表的是数字，则直接加到列表中
#     else:
#         i = i.replace('"','')
#         x,y = get_x(i)
#         #数字进行预处理
#         x = int(float(x))+6
#         y = int(float(y))+30
#         #print(x,y)
#         tel.append(get_num(svg,x,y))
# print(''.join(tel))#组成字符串


# #从css中获取svg的url，并构造成url
# res=re.search('.*?oul8fr', css.text, re.S)
# res=res.group(0)
# res=re.findall('url.*?\.svg',res,re.S)[-2]
# print(re.sub('url\(','http:',res))







# def get_urls():
#     headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive',  'Host': 'www.dianping.com', 'Referer': 'http', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
#     url='https://www.dianping.com/search/keyword/10/0_%E7%81%AB%E9%94%85'
#     res = requests.get(url,headers=headers)
#     res.encoding='utf-8'
#     html = etree.HTML(res.text)
#     urls= html.xpath('//div[@id="shop-all-list"]/ul/li/div[@class="pic"]/a/@href')
#     return urls
