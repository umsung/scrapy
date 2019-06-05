import logging, os, time
from selenium import webdriver


class Logger(object):
    def __init__(self, logger):
        self.logger = logging.Logger(logger)
        self.logger.setLevel(logging.DEBUG)

        sj = time.strftime('%y%m%d%H%M%S', time.localtime())
        log_path = os.path.dirname(os.path.abspath('.'))+'/logs/'
        # print(log_path)
        log_name = log_path + sj + '.log'
        fh = logging.FileHandler(log_name, encoding='utf-8')
        fh.setLevel(logging.INFO)

        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def getlog(self):
        return self.logger
