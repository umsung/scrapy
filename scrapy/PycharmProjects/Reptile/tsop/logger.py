import logging
import os.path
import time
import os

class Logger(object):

    def __init__(self, logger):
        # 创建logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)


        # 创建一个FileHandler， 用于写入文件日志
        sj = time.strftime('%y%m%d%H%M%S', time.localtime())
        log_path = os.path.dirname(os.path.abspath('.')) + '\Logs'
        print(log_path)
        log_name = log_path + sj + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)


        # 在创建一个控制台输出的StreamHandler
        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)


        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(sh)


    def get_log(self):
        return self.logger