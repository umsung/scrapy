from flask import Flask, url_for,jsonify,render_template
import random
import time
import celery
from celery import Celery

app = Flask(__name__)
# 配置

# 配置消息代理的路径，如果是在远程服务器上，则配置远程服务器中redis的URL
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
# 要存储 Celery 任务的状态或运行结果时就必须要配置
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
# 初始化Celery
celery = celery.Celery(app.name, broker = app.config['CELERY_BROKER_URL'])
# 将Flask中的配置直接传递给Celery
celery.conf.update(app.config)
# 上述代码中，通过 Celery 类初始化 celery 对象，传入的应用名称与消息代理的连接 URL。

# 通过 celery.task 装饰器装饰耗时任务对应的函数
# bind为True时，会传入self(Celery 本身)给被装饰的方法,可以用于记录与更新任务状态。
@celery.task(bind=True)
def long_task(self):
    # 耗时任务的逻辑
    verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
    adjective = ['master', 'radiant', 'silent', 'harmonic', 'fast']
    noun = ['solar array', 'particle reshaper', 'cosmic ray', 'orbiter', 'bit']
    message = ''
    total = random.randint(10,50)
    for i in range(total):
        if not message or random.random() < 0.25:    
        # 随机的获取一些信息
            message = '{1} {2} {3}'.format(random.choice(verb),random.choice(adjective),random.choice(noun))
        # 更新 Celery 任务的状态，这里使用了自定义状态「PROGRESS」，循环的数据信息通过 meta 参数 (元数据) 以字典的形式存储起来，到前端显示
        self.update_state(state='PROCESS', meta={'current':i, 'total':total,'message':message})
        time.sleep(1)
    return {'current':100, 'total':100,'status':'Task completed','result':200}

# Flask 中定义接口通过异步的方式执行耗时任务,
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

    # # delay () 与 apply_async () 会返回一个任务对象，该对象可以获取任务的状态与各种相关信息。
    # task = long_task.apply(1,2)

# 定义一个 Flask 接口方法来调用该耗时方法
@app.route('/longtask',methods=['GET','POST'])
def longtask():
    task = long_task.apply_async()
    # url_for url反转，指通过视图函数名称得到其对应的URL，第一个参数是函数名，第二个参数是url参数名
    return jsonify({}), 202, {'Location':url_for('taskstatus',task_id=task.id)}
    # 202 通常表示一个请求正在进行中，然后还在返回数据包的包头 (Header) 中添加了 Location 头信息，前端可以通过读取数据包中 Header 中的 Location 的信息来获取任务 id 对应的完整 url。


# 前端有了任务 id 对应的 url 后，还需要提供一个接口给前端，让前端可以通过任务 id 去获取当前时刻任务的具体状态。
@app.route('/status/<task_id>')
def taskstatus(task_id):
    # 使用任务 id 初始化 AsyncResult 类，获得任务对象，然后就可以从任务对象中获得当前任务的信息。
    # 该方法会返回一个 JSON，其中包含了任务状态以及 meta 中指定的信息，前端可以利用这些信息构建一个进度条。
    task = long_task.AsyncResult(task_id)
    if task.state == 'PENDING': # 在等待
        response = {
            'state':task.state,
            'current':0,
            'total':1,
            'message':'Pending'
        }
    elif task.state != 'FAILURE':
        response = {
            'state':task.state,
            # meta中的数据，通过task.info.get()可以获得 
            'current':task.info.get('current',0), # 当前循环进度
            'total':task.info.get('total',1),  # 总循环进度
            'message':task.info.get('message','')
        }
        if 'result' in task.info:
            response['result'] = task.info.get['result']
    else:
        response = {     
        # 后端执行任务出现了一些问题
            'state':task.state,
            'current':1,
            'total':1,
            'message':str(task.info)  # 报错的具体异常
        }
    return jsonify(response)

if __name__ == "__main__":
    app.run()