import requests
import re
from lxml import etree
import numpy as np
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Cookie': '__guid=169583271.388253713253878400.1534817461127.2454; _lxsdk_cuid=1655a3fe904ab-01904d5c1cf2fe-5d4e211f-100200-1655a3fe905c8; _lxsdk=1655a3fe904ab-01904d5c1cf2fe-5d4e211f-100200-1655a3fe905c8; _hc.v=44ef0c90-1a7b-d24c-1b86-87c1c2f6bd65.1534817463; s_ViewType=10; cy=10; cye=tianjin; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=1696aa54b17-4ec-56-0d2%7C%7C432', 'Host': 'www.dianping.com', 'If-Modified-Since': 'Sun, 10 Mar 2019 07', 'If-None-Match': '"555b6df9fea08164bb49fd7e966d99b3"', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
css_header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Host': 's3plus.meituan.net', 'If-Modified-Since': 'Wed, 06 Mar 2019 14', 'If-None-Match': '"4684b1c3dee8f4d172b2ac0c11e827a1"', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

def get_css():
    response = requests.get('http://www.dianping.com/shop/97404408', headers=headers).text
    html = etree.HTML(response)
    css_url = html.xpath('//link[@rel="stylesheet"]/@href')
    print(css_url)
    # return 'http:' + css_url[1]
    css = requests.get('http:' + css_url[1], headers=css_header)
    css.encoding = 'utf-8'
    return css.text


def get_svg(css_text):
    # res = re.search('.*?oul8fr', css_text, re.S)
    # print(res)
    # res = res.group(0)
    res = re.findall(r'url.*?\.svg', css_text, re.S)[-2]
    print(res)
    url = re.sub('url\(', 'http:', res, re.S)
    response = requests.get(url).content
    return response


if __name__ == '__main__':
    css_text = get_css()
    print(css_text)
    get_svg(css_text)