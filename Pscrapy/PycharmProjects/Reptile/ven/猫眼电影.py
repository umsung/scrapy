import requests
from lxml import etree
import csv
import os


def page_num(n):
    url = 'http://maoyan.com/board/4?offset={}'.format(n)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html = response.content.decode(response.apparent_encoding)
    selector = etree.HTML(html)
    mov_list = selector.xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
    f = open('猫眼电影.csv', 'a', encoding='utf-8', newline='')
    w = csv.writer(f)
    for mov in mov_list:
        mov_img = mov.xpath('.//img[@class="board-img"]/@data-src')[0]
        mov_name = mov.xpath('.//p[@class="name"]/a/text()')[0]
        mov_name_href = url.split('/b')[0] + mov.xpath('.//p[@class="name"]/a/@href')[0]
        mov_star = mov.xpath('.//p[@class="star"]/text()')[0]
        mov_date = mov.xpath('.//p[@class="releasetime"]/text()')[0]
        try:
            os.mkdir('cat_eye_move')
        except FileExistsError:
            pass
        with open('./cat_eye_move/{}.jpg'.format(mov_name), 'wb') as i:
            i.write(requests.get(mov_img).content)
        # print(mov_img, mov_name,mov_name_href, mov_star, mov_date)
        l = []
        l.append(mov_img)
        l.append(mov_name)
        l.append(mov_name_href)
        l.append(mov_star)
        l.append(mov_date)
        w.writerow(l)


if __name__ == '__main__':
    f = open('猫眼电影.csv', 'w', encoding='utf-8', newline='')
    for i in range(10):
        page_num(i * 10)
