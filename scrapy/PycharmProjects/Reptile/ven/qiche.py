# coding:utf-8
import re
import requests
from lxml import etree
from fontTools.ttLib import TTFont

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 "
              "Safari/537.36 "
}

url = 'https://club.autohome.com.cn/bbs/thread/1d0784305887ec3f/72381110-1.html#pvareaid=102410'

# 请求内容
response = requests.get(url, headers=headers)
response_html = response.content.decode('gbk')
# print(response_html)
# xpath 获取帖子内容
response_xml = etree.HTML(response_html)
content_list = response_xml.xpath('//div[@class="conttxt"]/div[1]//text()')
print(content_list)
content_str = ''.join(content_list)
print(content_str)

# 获取字体的连接文件
fonts_ = re.search(r",url\('(//.*\.ttf)?'\) format",response_html).group(1)

# 请求字体文件， 字体文件是动态更新的
fonts_url = 'https:'+fonts_
response = requests.get(fonts_url, headers=headers).content
# 讲字体文件保存到本地
with open('fonts.ttf', 'wb') as f:
    f.write(response)

# 解析字体库
font = TTFont('fonts.ttf')

# 读取字体的映射关系
uni_list = font['cmap'].tables[0].ttFont.getGlyphOrder()
print('uni_list',uni_list)

# 转换格式
utf_list = [eval(r"u'\u" + x[3:] + "'") for x in uni_list[1:]]
print('utf_list',utf_list)
# 被替换的字体的列表
word_list = [u'一', u'七', u'三', u'上', u'下', u'不', u'九', u'了', u'二', u'五', u'低', u'八', u'六',
         u'十', u'的', u'着', u'近', u'远', u'长', u'右', u'呢', u'和', u'四', u'地', u'坏', u'多',
         u'大', u'好', u'小', u'少', u'短', u'矮', u'高', u'左', u'很', u'得', u'是', u'更']
#遍历需要被替换的字符
for i in range(len(utf_list)):
    content_str = content_str.replace(utf_list[i], word_list[i])

print(content_str)
