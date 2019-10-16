#文件db的内容为：{"count":1}
#注意一定要用双引号，不然json无法识别
from multiprocessing import Process,Lock
import time,json,random
import os
from json import JSONDecodeError

def search():
    dic=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'db.txt')))
    print('\033[43m剩余票数%s\033[0m' %dic['count'])

def get():
    try:
        dic=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'db.txt')))
        time.sleep(0.1) #模拟读数据的网络延迟
        if dic['count'] >0:
            dic['count']-=1
            time.sleep(0.2) #模拟写数据的网络延迟
            json.dump(dic,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'db.txt'),'w'))
            print('\033[43m购票成功\033[0m')
        else:
            print('\033[43m无票\033[0m')
    except JSONDecodeError:
        print('jsondecodeError')

def task(lock):
    search()
    lock.acquire()
    get()
    lock.release()

if __name__ == '__main__':
    lock=Lock()
    for i in range(100): #模拟并发100个客户端抢票
        p=Process(target=task,args=(lock,))
        p.start()