from multiprocessing import Process,Pool,Lock
import os,time

def process_function(name):
    print('%s is running %s' % (os.getpid(), name))
    time.sleep(0.5)
    print('%s is done %s' %(os.getpid(),name))

if __name__ == "__main__":
    for i in range(3):
        p = Process(target=process_function, args=(i,))
        p.start()