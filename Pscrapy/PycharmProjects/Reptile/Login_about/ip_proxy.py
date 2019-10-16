import requests
from scrapy.selector import Selector
import pymysql

# 链接mysql数据库
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='mysql18_text', charset='utf8')
cursor = conn.cursor()

def crawl_ips():
    # 爬取xici的免费ip代理,存入数据库
    agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0'
    header = {
        'User-Agent': agent
    }

    for i in range(1, 3458):
        reas = requests.get('http://www.xicidaili.com/nn/', headers=header)
        Selectora = Selector(reas)
        all_trs = Selectora.xpath('//table[@id="ip_list"]/tr')
        ip_list = []
        for tr in all_trs[1:]:
            spend_str = tr.xpath('./td/div[@class="bar"]/@title').extract()[0]  ##提取速度
            if spend_str:
                speed = float(spend_str.split('秒')[0])
                all_text = tr.xpath('./td/text()').extract()
                ip = all_text[0]
                port = all_text[1]
                proxy_type = all_text[5]
                ip_list.append((ip, port, speed, proxy_type))
        for ip_info in ip_list:
            cursor.execute(
                """insert project_ip(ip,port,speed,proxy_type) VALUES('{0}','{1}','{2}','HTTP')""".format(
                    ip_info[0], ip_info[1], ip_info[2]
                )
            )
            conn.commit()
        print(ip_list)


crawl_ips()

conn.close()
cursor.close()


# 随机获取上面存到数据库的ip，如果不能用就删除，能用就用

class GetIP(object):
    def delete_ip(self, ip):
        # 从数据库中删除无效的ip
        delete_sql = """delete from project_ip where ip='{0}'""".format(ip)
        cursor.execute(delete_sql)
        conn.commit()
        return True

    def judge_ip(self, ip, port):
        # 判断一个ip是否可用
        http_url = 'http://www.baidu.com'
        proxy_url = 'https://{0}:{1}'.format(ip, port)

        try:
            proxy_dict = {
                'http': proxy_url,
            }
            response = requests.get(http_url, proxies=proxy_dict)
            # return True
        except Exception as e:
            print("ip出现异常")
            # 出现异常后就把这个ip给删除掉
            self.delete_ip(ip)
            return False
        else:
            code = response.status_code
            if code >= 200 and code < 300:
                print('effective ip')
                return True
            else:
                print('invalid')
                self.delete_ip(ip)
                return False

    def get_random_ip(self):
        # 从数据库中随机获取到一个可用的ip
        random_sql = """SELECT ip,port FROM project_ip ORDER BY RAND() LIMIT 1"""
        result = cursor.execute(random_sql)

        for ip_info in cursor.fetchall():
            ip = ip_info[0]
            port = ip_info[1]
            judge_re = self.judge_ip(ip, port)
            if judge_re:
                return "http://'{0}':'{1}'".format(ip, port)
            else:
                return self.get_random_ip()
