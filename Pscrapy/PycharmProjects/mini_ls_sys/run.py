from PycharmProjects.mini_ls_sys.stock import Stock
from PycharmProjects.mini_ls_sys.mail import Mail
import threading
from multiprocessing import Process, Pool, Queue
import time
from datetime import datetime

q = Queue()
stock = Stock(q,10000)
mail = Mail()

def send():
    start_time = datetime(datetime.now().year,datetime.now().month,datetime.now().day,hour=9,minute=30,second=0)
    end_time = datetime(datetime.now().year,datetime.now().month,datetime.now().day,hour=15,minute=0,second=0)
    cur_time = datetime.now()
    h_price = ''
    l_price= ''
    while True:
        if  cur_time < start_time or cur_time>end_time:
            print('不在时间范围内')
            stock.stop_run()
            break
        if  not q.empty():
            cur_price = q.get()
            if cur_price<l_price or cur_price > h_price:
                mail_content = '当前价格:{}， 范围是{}-{}'.format(cur_price,l_price,h_price)
                mail.mail_content = mail_content
                mail.send_mail()
                time.sleep(10)


p1 = Process(target=stock.start_run)
p2 = Process(target=send)
p1.start()
p2.start()
p1.join()
p2.join()