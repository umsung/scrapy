import requests
from lxml import etree
import csv
import os
from multiprocessing import Pool
import time

def parar(url):
    # url = 'https://db.yaozh.com/fangji/10000001.html'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'kztoken=nJail6zJp6iXaJqWl25maGlpZJub; his=a%3A10%3A%7Bi%3A0%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maGdvYZeS%22%3Bi%3A1%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maGdvYZeV%22%3Bi%3A2%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maGdvY5OW%22%3Bi%3A3%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maGdwZpmX%22%3Bi%3A4%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maGhxZJmX%22%3Bi%3A5%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maGloYpia%22%3Bi%3A6%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maGloY5WS%22%3Bi%3A7%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maGloapSU%22%3Bi%3A8%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maGloapSb%22%3Bi%3A9%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maGlpZJub%22%3B%7D; acw_tc=2f624a0b15547779373626962e2c454f3d12c9a51208a2d9d43b5811aad164; _ga=GA1.2.914088002.1554777939; MEIQIA_EXTRA_TRACK_ID=1Jby9OhcHRDm9UapjQCJf6v4k7q; PHPSESSID=em2sotpr6k17674abrsevufg56; _gid=GA1.2.1753007927.1554858488; yaozh_userId=726973; UtzD_f52b_saltkey=KcT6zzbc; UtzD_f52b_lastvisit=1554854893; _ga=GA1.3.914088002.1554777939; bigdata_use_tips=1; UtzD_f52b_ulastactivity=1554775927%7C0; UtzD_f52b_creditnotice=0D0D2D0D0D0D0D0D0D656992; UtzD_f52b_creditbase=0D0D2D0D0D0D0D0D0; UtzD_f52b_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; think_language=zh-CN; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1554777939,1554858363,1554879242; MEIQIA_VISIT_ID=1JfHUFPWGzr0pnXODvkRcAvLM3Y; expire=1554896537641; yaozh_logintime=1554879276; yaozh_user=726973%09a13570341204; db_w_auth=656992%09a13570341204; UtzD_f52b_lastact=1554879277%09uc.php%09; UtzD_f52b_auth=ed8aJNCDbiS%2FUCUPTICp%2FuB2Ny3FHfnSK5H%2FYaAAdNzgh%2FlHln3qXjF96LYZVWPIIJ6Tiaobtpbbh5dZeHkW%2FN0hZj8; kztoken=nJail6zJp6iXaJqWl25maGloaZub; his=a%3A10%3A%7Bi%3A0%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maGduapyT%22%3Bi%3A1%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maGduapyW%22%3Bi%3A2%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maGdvYZeS%22%3Bi%3A3%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maGdvYZeV%22%3Bi%3A4%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maGdvY5OW%22%3Bi%3A5%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maGdwZpmX%22%3Bi%3A6%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maGhxZJmX%22%3Bi%3A7%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maGloYpia%22%3Bi%3A8%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maGloY5WS%22%3Bi%3A9%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maGloaZub%22%3B%7D; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1554881392',
        'Host': 'db.yaozh.com',
        'Referer': 'https://db.yaozh.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }
    Cookie = {
        'Cookie': 'kztoken=nJail6zJp6iXaJqWl25maWVuaZOZ; his=a%3A10%3A%7Bi%3A0%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZZeT%22%3Bi%3A1%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZZuZ%22%3Bi%3A2%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpaW%22%3Bi%3A3%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpeS%22%3Bi%3A4%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpqW%22%3Bi%3A5%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpuT%22%3Bi%3A6%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpuY%22%3Bi%3A7%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZ5OT%22%3Bi%3A8%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuaZOS%22%3Bi%3A9%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuaZOZ%22%3B%7D; acw_tc=2f624a0b15547779373626962e2c454f3d12c9a51208a2d9d43b5811aad164; _ga=GA1.2.914088002.1554777939; MEIQIA_EXTRA_TRACK_ID=1Jby9OhcHRDm9UapjQCJf6v4k7q; _gid=GA1.2.1753007927.1554858488; UtzD_f52b_saltkey=KcT6zzbc; UtzD_f52b_lastvisit=1554854893; _ga=GA1.3.914088002.1554777939; bigdata_use_tips=1; UtzD_f52b_ulastactivity=1554775927%7C0; think_language=zh-CN; PHPSESSID=554uh18imjkus745n6barrf2n3; UtzD_f52b_creditnotice=0D0D2D0D0D0D0D0D0D656992; UtzD_f52b_creditbase=0D0D4D0D0D0D0D0D0; UtzD_f52b_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; MEIQIA_VISIT_ID=1JhRsmsBJRpXRK5aPLR1eYfaG3U; expire=1554962834212; UtzD_f52b_lastact=1554946013%09uc.php%09; yaozh_logintime=1554946364; yaozh_user=728478%09umsung; yaozh_userId=728478; yaozh_uidhas=1; yaozh_mylogin=1554946365; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1554946367; acw_tc=2f624a6715548584856626296e3d7bf5fd4df0e048c213322b156b89e54150; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1554858363%2C1554879242%2C1554945547%2C1554946367; kztoken=nJail6zJp6iXaJqWl25maWVuZ5qa; his=a%3A10%3A%7Bi%3A0%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZZWV%22%3Bi%3A1%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZZeT%22%3Bi%3A2%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZZuZ%22%3Bi%3A3%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpaW%22%3Bi%3A4%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpeS%22%3Bi%3A5%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpqW%22%3Bi%3A6%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpuT%22%3Bi%3A7%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpuY%22%3Bi%3A8%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZ5OT%22%3Bi%3A9%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZ5qa%22%3B%7D'
    }

    requests.packages.urllib3.disable_warnings()
    try:
        resp = requests.get(url, headers=headers, cookies=Cookie, verify=False)
        if resp.status_code == 200:
            return resp.text
        else:
            return None
    except ConnectionError:
        print("error occur")
        return None


def param_html(html, url):
    selector = etree.HTML(html)
    f = open('c.csv', 'a', encoding='utf-8', newline='')
    w = csv.writer(f)
    itme = {}

    itme['a'] = selector.xpath("//*[contains(./th/text(), '方名')]/td/span/text()")
    itme['a'] = ''.join(itme['a']).strip()
    itme['b'] = selector.xpath("//*[contains(./th/text(), '规范名')]/td/span/text()")
    itme['b'] = ''.join(itme['b']).strip()
    itme['c'] = selector.xpath("//*[contains(./th/text(), '经典')]/td/span/text()")
    itme['c'] = ''.join(itme['c']).strip()
    itme['d'] = selector.xpath("//*[contains(./th/text(), '出处')]/td/span/text()")
    itme['d'] = ''.join(itme['d']).strip()
    itme['e'] = selector.xpath("//*[contains(./th/text(), '功用大类')]/td/span/text()")
    itme['e'] = ''.join(itme['e']).strip()
    itme['f'] = selector.xpath("//*[contains(./th/text(), '功用小类')]/td/span/text()")
    itme['f'] = ''.join(itme['f']).strip()
    itme['g'] = selector.xpath("//*[contains(./th/text(), '处方')]/td/span/text()")
    itme['g'] = ''.join(itme['g']).strip()
    itme['h'] = selector.xpath("//*[contains(./th/text(), '炮制')]/td/span/text()")
    itme['h'] = ''.join(itme['h']).strip()
    itme['i'] = selector.xpath("//*[contains(./th/text(), '功用')]/td/span/text()")
    itme['i'] = ''.join(itme['i']).strip()
    itme['j'] = selector.xpath("//*[contains(./th/text(), '主治')]/td/span/text()")
    itme['j'] = ''.join(itme['j']).strip()
    itme['k'] = selector.xpath("//*[contains(./th/text(), '方解')]/td/span/text()")
    itme['k'] = ''.join(itme['k']).strip()
    itme['m'] = selector.xpath("//*[contains(./th/text(), '禁忌')]/td/span/text()")
    itme['m'] = ''.join(itme['m']).strip()
    itme['n'] = selector.xpath("//*[contains(./th/text(), '化裁')]/td/span/text()")
    itme['n'] = ''.join(itme['n']).strip()
    itme['o'] = selector.xpath("//*[contains(./th/text(), '附方')]/td/span/text()")
    itme['o'] = ''.join(itme['o']).strip()
    itme['p'] = selector.xpath("//*[contains(./th/text(), '附注')]/td/span/text()")
    itme['p'] = ''.join(itme['p']).strip()
    itme['q'] = selector.xpath("//*[contains(./th/text(), '文献')]/td/span/text()")
    itme['q'] = ''.join(itme['q']).strip()
    itme['r'] = selector.xpath("//*[contains(./th/text(), '运用')]/td/span/text()")
    itme['r'] = ''.join(itme['r']).strip()
    itme['s'] = selector.xpath("//*[contains(./th/text(), '用法用量')]/td/span/text()")
    itme['s'] = ''.join(itme['s']).strip()
    itme['t'] = selector.xpath("//*[contains(./th/text(), '备注')]/td/span/text()")
    itme['t'] = ''.join(itme['t']).strip()
    itme['url'] = url
    print(itme)
    w.writerow(itme.values())


def main(num):
    # url = 'https://db.yaozh.com/fangji/{}.html'
    # for i in range(5056, 6001):
    #     num = 10000000 + i
    #     print('正在爬取第{}页'.format(i))
    #     html = parar(url.format(num))
    #     param_html(html, url.format(num))
    #     time.sleep(0.2)
    url = 'https://db.yaozh.com/fangji/' + str(num) + '.html'
    print('正在采集第{}页'.format(num))
    html = parar(url)
    param_html(html, url)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i for i in range(10006001, 10009001)])
    # main()
