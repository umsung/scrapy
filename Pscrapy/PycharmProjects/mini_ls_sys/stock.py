# 实时获取股票数据

# 连接邮件服务器

# 预警配置管理 

# 监控数据并发送邮件
import tushare as ts
import time
from datetime import datetime


class Stock(object):
    def __init__(self,q,stock_num='10000'):
        self.q = q
        self.stock_num = stock_num
        self._terminal = True

    def query_stock_read_price(self):
        df = ts.get_realtime_quotes(self.stock_num)
        df = df[['price','time']]
        price = df['price'][0]   # df['price'][0] == df['price'].values[0]
        time = df['time'][0]
        return price,time
    
    def get_kline_data(self,ktype=""):
        today = datetime.now().strftime('%y-%m-%d')
        df = ts.get_hist_data(self.stock_num, start='2019-05-01', end=today)
        return df[ktype]

    def start_run(self):
        while self._terminal:
            p,t = self.query_stock_read_price()
            print('{}: stock price is {}'.format(t,p))
            self.q.put(float(p))
            time.sleep(1)

    def stop_run(self):
        self._terminal=False