import threading
import logging
import time
import concurrent.futures

# 线程池创建多线程

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H%M%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as excutor:
        excutor.map(thread_function, range(4))
