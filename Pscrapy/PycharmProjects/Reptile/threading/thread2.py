import threading
import logging
import time


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H%M%S")
    logging.info('Main    : before creating thread')
    t = threading.Thread(target=thread_function, args=(1,), daemon=True)
    logging.info('Main    : threading start before')
    t.start()
    logging.info('Main    : wait for the thread to finish')
    t.join()
    logging.info('Main    : all done')