import threading
import logging
import time
import concurrent.futures
import random


class Pipeline(object):
    def __init__(self):
        self.message=0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()
    
    def get_message(self, name):
        self.consumer_lock.acquire()
        message = self.message
        self.producer_lock.release()
        return message

    def set_message(self, message, name):
        self.producer_lock.acquire()
        self.message = message
        self.consumer_lock.release()
     

SENTINEL = object()

def producer(pipeline):
    for i in range(10):
        message = random.randint(1,100)
        pipeline.set_message(message, 'producer')
        logging.debug("producer set message %s to pipeline" %message)
    pipeline.set_message(SENTINEL, 'producer')

    
def consumer(pipeline):
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message('consumer')
        if message is not SENTINEL:
            logging.info("consumer get message %s from pipeline" %message)



if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, datefmt="%H%M%S", level=logging.DEBUG)
    pipeline = Pipeline()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as excutor:
        excutor.submit(producer,pipeline)
        excutor.submit(consumer,pipeline)