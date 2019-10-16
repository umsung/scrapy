from multiprocessing import Process, Queue
import os, time, random


def write(q):
    print('start write %s' % (os.getpid()))
    for i in ['A', 'B', 'C']:
        print('write %s to Queue' % i)
        q.put(i)
        time.sleep(random.random())


def write1(q):
    print('start read %s' %(os.getpid()))
    for i in ['A', 'B', 'C']:
        print('write %s to Queue' % i)
        q.put(i)
        time.sleep(random.random())


def read1(q):
    print('start read %s' %(os.getpid()))
    while True:
        value = q.get(True)
        print('get %s from Queue' %value)


def read(q):
    print('start read {}'.format(os.getpid()))
    while True:
        value = q.get(True)
        print('get %s from Queue' % value)


if __name__ == '__main__':
    q = Queue()
    one = Process(target=write, args=(q,))
    two = Process(target=read, args=(q,))
    one.start()
    two.start()
    one.join()
    two.terminate()
