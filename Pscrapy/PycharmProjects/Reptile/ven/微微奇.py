import requests
from lxml import etree
import csv
import os

url = 'http://www.weiweiqi.com/'
response = requests.get(url)
html = response.content.decode(response.apparent_encoding)
selector = etree.HTML(html)
node_list = selector.xpath('/html/body/div[2]/div[1]/ul/li')

f = open('微微奇.csv', 'w', encoding='utf-8', newline='')
w = csv.writer(f)

for node in node_list:
    node_img=node.xpath('./a/img/@src')[0]
    try:
        os.mkdir('img')
    except FileExistsError:
        pass
    with open('./img/{}'.format((node_img.split('/'))[-1]),'wb') as i:
        i.write(requests.get(node_img).content)
    node_title = node.xpath('./h2/a/text()')[0]
    node_href = node.xpath('./h2/a/@href')[0]
    node_info = node.xpath('./p/text()')[0]
    l=[]
    l.append(node_title)
    l.append(node_href)
    l.append(node_info)
    w.writerow(l)

