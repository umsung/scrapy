#-*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import os
import csv
from multiprocessing import Pool


def get_html(url):
    try:

        resp = requests.get(url)
#        resp.encoding = "utf-8"
        if resp.status_code == 200:
            return resp.content.decode('utf-8')
            #print(resp.content.decode('utf-8'))
        return None
    except ConnectionError:
        print("error occur")
        return None


def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    lis = soup.select('ul.excerpt > li')
    print(lis)
    f = open('琪琪cc.csv', 'a', encoding='utf-8', newline='')
    w = csv.writer(f)
    head = ['img_href', 'b_name', 'n_href', 'abstract_name', 'b_time']
    w.writerow(head)
    for item in lis:
        a = []
        img_href = item.find('a', class_='pic').find('img').get('src')
        b_name = item.find('h2', class_='excerpt-tit').text.strip()
        name_href = item.find('h2','excerpt-tit').find('a').get('href')
        abstract_name = item.find('p', class_='excerpt-desc').text.strip()
        b_time = item.find('div', class_='excerpt-time').text[3:]
        n_href = item.select('h2.excerpt-tit > a')[0].get('href')
        try:
            os.mkdir('img_file')
        except FileExistsError:
            pass
        with open('./img_file/{}.jpg'.format(b_name), 'wb') as f:
            f.write(requests.get(img_href).content)
        a.append(img_href)
        a.append(b_name)
        a.append(n_href)
        a.append(abstract_name)
        a.append(b_time)
        w.writerow(a)
 #       print(a)


def main(num):
    url = 'http://www.weiweiqi.com/page/' + str(num)
    html = get_html(url)
    parse_html(html)
  #  print('中文')


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [item for item in range(1, 5)])
 #   main()