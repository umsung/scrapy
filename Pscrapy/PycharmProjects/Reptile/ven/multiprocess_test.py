from multiprocessing import Process, Pool
import os
import time
import random

def run_proc(name):
    print('Run child process %s (%s)' %(name, os.getpid()))
    start_time = time.time()
    time.sleep(random.random()*3)
    end_time = time.time()
    print('Task %s runs %0.2f seconds' % (name, (end_time-start_time)))


if __name__ == '__main__':
    print('parent process start %s' % (os.getpid()))
    # p = Process(target=run_proc, args=('test',))
    p = Pool(4)
    for i in range(5):
        p.apply_async(run_proc, args=(i,))
    print('will start')
    p.close()
    p.join()
    print('end')