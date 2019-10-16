from concurrent.futures import ThreadPoolExecutor
from flask import Flask
import time

# 创建线程池执行器
exector = ThreadPoolExecutor(3)
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return 'Welcome to test page'

@app.route('/job')
def run_jobs():
    # 交由线程去执行耗时任务
    exector.submit(long_task,'hello','mao')
    return 'long task running'

def long_task(args1,args2):
    print('args: %s,%s' %(args1,args2))
    time.sleep(5)
    print('task is done')

if __name__ == "__main__":
    app.run()