import requests
from lxml import etree
import csv

url = 'https://hr.tencent.com/position.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36'
}
# 发送请求
response = requests.get(url, headers=headers)
# 得到响应，转为字符串类型
html = response.content.decode(response.apparent_encoding)
# 构建DOM树
selector = etree.HTML(html)
node_list = selector.xpath('//*[@id="position"]/div[1]/table//tr[@class="even" or @class="odd"]')
f = open('腾讯社招2.csv', 'w', encoding='utf-8', newline='')
w = csv.writer(f)
for node in node_list:
    # job_name = node.xpath('./td[1]/a/text()')[0]
    # job_class = node.xpath('./td[2]/text()')[0]
    # job_num = node.xpath('./td[3]/text()')[0]
    # job_address = node.xpath('./td[4]/text()')[0]
    # job_time = node.xpath('./td[5]/text()')[0]
    # print(job_name, job_class, job_num, job_address, job_time)
    # l=[]
    # l.append(job_name)
    # l.append(job_class)
    # l.append(job_num)
    # l.append(job_address)
    # l.append(job_time)
    # w.writerow(l)
    job_name = node.xpath('./td[1]/a/text()')
    job_class = node.xpath('./td/text()')
    print(job_name, job_class)
    w.writerow((job_name + job_class))
