from flask import Flask, g
from db import *
from config import *
import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route('/')
def index():
    return '<h2>Welcome to Cookie Pool System</h2>'


def get_conn():
    for i in GENERATOR_MAP:
        if not hasattr(g, i):
            setattr(g, i+'_cookies', eval('CookiesRedisClient'+ '(name ="'+ i +'")'))
            setattr(g, i+'_account', eval('AccountRedisClient'+ '(name="' + i + '")' ))
    return g

@app.route('/<name>/random')
def get(name):
    g = get_conn()
    cookies = getattr(g, name+'_cookies').random()
    return cookies

@app.route('/<name>/count')
def count(name):
    g = get_conn()
    count = getattr(g, name+'_cookies').count()
    return count if isinstance(count,str) else str(count)

@app.route('/<name>/add_ac/<username>/<password>')
def add_user(name,username,password):
    g = get_conn()
    result = getattr(g, name+'_account').set(username,password)
    if result:
        return 'add user success'
    else:
        return 'add user fail'

@app.route('/<name>/add_co/<username>/<cookies>')
def add_cookies(name,username,cookies):
    g = get_conn()
    result = getattr(g, name+'_cookies').set(username,cookies)
    if result:
        return 'add cookies success'
    else:
        return 'add cookies fail'


if __name__ == "__main__":
    app.run()