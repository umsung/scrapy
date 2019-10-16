import threading
import logging
import time
import concurrent.futures

# 线程池创建多线程，竞态条件, 线程池ThreadPoolExecutor作为上下文管理器，使用锁lock作为上下文管理器

class Fakedatabase(object):
    def __init__(self):
        self.value=0
        self._lock =threading.Lock()

    def update(self,name):
        logging.info("Thread %s: Starting  update", name)
        with self._lock:
            logging.debug("Thread %s: has  lock", name)
            local_copy=self.value
            local_copy +=1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug("Thread %s: about to release  lock", name)
        time.sleep(0.5)
        logging.debug("Thread %s: after to release  lock", name)
        logging.info("Thread %s: finishing update", name)


if __name__ == "__main__":
    
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H%M%S")
    logging.getLogger().setLevel(logging.DEBUG)
    f = Fakedatabase()
    logging.info("Testing update. Starting  value is %d.", f.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as excutor:
        for i in range(3):
            excutor.submit(f.update, i)
        # excutor.map(f.update,range(3))  另一种写法
    
    logging.info("Testing update. Ending value is %d.", f.value)
