import pymysql
import requests
from scrapy.selector import Selector

class MysqlClient(object):
    def __init__(self,host='',user='',db='', table='default'):
        self.conn = pymysql.connect(host=host,user=user,db=db,charset='utf-8')
        self.cursor = self.conn.cursor()
        self.table = table

    def select_random(self):
        result = self.cursor.execute('''select * from %s order by rand() limit 1 ''' %self.table)
        return result

    def insert(self,ip,port):
        self.cursor.execute(''' insert into %s(ip,port) values(%s,%s) ''' %(self.table,ip,port))

    def delete_ip(self,ip):
        self.cursor.execute(''' delete from %s where ip =%s''' %(self.table,ip))
    