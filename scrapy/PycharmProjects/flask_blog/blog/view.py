from blog import app
from blog import db
from blog.models import User
from flask import render_template, flash, redirect, session, url_for, request, g
from blog.templates import *

@app.route('/')
def index():
    return 'Hello Duan'


@app.route('/adduser/<nickname>/<email>')
def adduser(nickname, email):
    u = User(neckname=nickname, email=email)
    try:
        db.session.add(u)
        db.session.commit()
        return 'add successful'
    except:
        return 'something go wrong'

# 插入新建数据
@app.route('/insert/')
def insert():
    user1 = User(id=7, neckname='testname7', email='2227@qq.com', role='7')
    user2 = User(id=8, neckname='testname8', email='2228@qq.com', role='8')
    db.session.add_all([user1, user2])
    db.session.commit()
    return 'successful'

# 更新数据
@app.route('/update/<uid>/<name>')
def update(uid, name):
    user = User.query.get(uid)
    # user = User.query.get(uid).update({'neckname':'test'})
    # db.session.delete(user)
    if user:
        user.neckname = name
        db.session.add(user)
        db.session.commit()
        return '修改成功'
    else:
        return '修改失败'


@app.route('/find/')
def find():
    lists = User.query.all()
    data = ';'.join([str(i.id) for i in lists])
    return data


# 条件查询
@app.route('/xfind/')
def xfind():
    list = User.query.filter_by(role=1).all()
    data = ';'.join([str(i.id) for i in list])
    return data


# @app.route('/dosql/')
# def dosql():
#     re = db.session.excute('select id, neckname from user')


@app.route('/getuser/<nickname>')
def getuser(nickname):
    user = User.query.filter_by(neckname=nickname).first()
    return render_template('user.html', user=user)


@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


@app.route('/test/<param>')
def test(param):
    roles = User.query.all()
    return render_template('user.html', user=roles)


@app.route('/d')
def index1():

    render_template('index1.html')



