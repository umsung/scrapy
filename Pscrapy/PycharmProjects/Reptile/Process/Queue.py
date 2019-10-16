from multiprocessing import Process, JoinableQueue,Queue
import time
import random
import os
import multiprocessing
# JoinableQueue 是  Queue的子类

def get(q):
    name = multiprocessing.current_process().name
    while True:
        d = q.get()
        print('%s get %s' %(name, d))
        time.sleep(random.randint(1,2))
        q.task_done()  # 向q.join()发送一次信号,证明一个数据已经被取走了
        
        
def put(q):
    name = multiprocessing.current_process().name
    for i in range(3):
        print('%s put %s' %(name,i))
        q.put(i)
        # time.sleep(random.randint(1,3))
    q.join()  # 生产者调用此方法进行阻塞，直到队列中所有的项目均被处理。阻塞将持续到队列中的每个项目均调用q.task_done（）方法为止

if __name__ == "__main__":
    print('main peocess is %s' % os.getpid())
    q = Queue()
    j = JoinableQueue()
    p1 = Process(target=put, args=(j,), name='p1')
    p2 = Process(target=put, args=(j,), name = 'p2')
    p3 = Process(target=put, args=(j,), name = 'p3')
    g1 = Process(target=get, args=(j,), name = 'g1')
    g2 = Process(target=get, args=(j,), name = 'g2', daemon=True)

    g1.daemon = True
    
    for i in [p1,p2,p3,g2,g1]:
        i.start()
    
    p1.join()
    p2.join()
    p3.join()
    print('mask done')
