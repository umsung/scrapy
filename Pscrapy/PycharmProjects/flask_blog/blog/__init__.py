# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blog.setting import basedir


app = Flask(__name__)

# 加载配置文件内容
app.config.from_object('blog.setting')

# 创建数据库对象
db = SQLAlchemy(app)


from blog import view, models
# # import  os
# # print os.environ.keys()
# # print os.environ.get('FLASKR_SETTINGS')
# # 加载配置文件内容
# app.config.from_object('blog.setting')     # 模块下的setting文件名，不用加py后缀
# app.config.from_envvar('FLASKR_SETTINGS')   # 环境变量，指向配置文件setting的路径
#
# # 创建数据库对象
# db = SQLAlchemy(app)