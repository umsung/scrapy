# _*_ coding: utf-8 _*_

# #调试模式是否开启
# DEBUG = True
#
# SQLALCHEMY_TRACK_MODIFICATIONS = False
# #session必须要设置key
# SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
#
# #mysql数据库连接信息,这里改为自己的账号
# SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost:3306/DBname"

import os

#  连接数据库引擎配置

# 数据库路径
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/flask"
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'dp.repository')
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# 配置数据库类型及路径
# databasetype+driver://user:password@ip:port/db_name
#
# 对于你在之前安装的每个驱动程序来说，对应的URI会是：
#
# #SQLite
#
# sqlite:///database.db
#
# #MySQL
#
# mysql+pymysql://user:password@ip:port/db_name
#
# #Postgres
#
# postgresql+psycopg2://user:password@ip:port/db_name
#
# #MSSQL
#
# mssql+pyodbc://user:password@dsn_name
#
# #Oracle
#
# oracle+cx_oracle://user:password@ip:port/db_name




# SQLALCHEMY_DATABASE_URI是the Flask-SQLAlchemy必需的扩展。这是我们的数据库文件的路径。
#
# SQLALCHEMY_MIGRATE_REPO 是用来存储SQLAlchemy-migrate数据库文件的文件夹。

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True