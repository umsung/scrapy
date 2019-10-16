from multiprocessing import Process, Pool, Queue
import os,time,random
import multiprocessing

def put(q):
    print('thread id: %s' % os.getpid())
    for i in range(3):
        time.sleep(random.randint(0,1))
        q.put(i)
        print('%s put %s' %(os.getpid(), i))
    q.put(None)

def get(q):
    print('thread id: %s' % os.getpid())
    while True:
        time.sleep(random.randint(0,1))
        res = q.get()
        if res == None:
            break
        print('%s get %s' %(os.getpid(), res))


if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=put, args=(q,))
    p2 = Process(target=get, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
