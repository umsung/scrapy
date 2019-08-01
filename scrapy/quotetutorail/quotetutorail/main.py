import os
import time

while True:
    os.system('scrapy crawl  项目1')
    print('启动项1')

    os.system('scrapy crawl 项目1')
    print('启动项2')

    time.sleep(100)