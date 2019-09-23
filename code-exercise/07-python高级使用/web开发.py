# -*- coding:utf-8 -*-

"""
Name: web开发.py
Author: fengdi
Datetime: 19:50 2019/5/14 
Description:主要介绍web开发的相关内容

"""
from flask import Flask
from flask import request
from flask import render_template
from wsgiref.simple_server import make_server

# wsgi接口

# wsgi处理函数


def application(environ, start_response):
    start_response('200 ok', [('Content-Type', 'text/html')])
    return [b'<h1>Hello web!</h1>']


# wsgi服务器代码
# 创建wsgi服务器，加载处理函数
httpd = make_server('', 8000, application)
print('Serving  HTTP on port 8000...')

# 监听HTTP请求
httpd.serve_forever()


# web框架：flask


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h2>Home</h2>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action='/signin' method='post'>
              <p><input name='username'></p>
              <p><input name='password' type='password'></p>
              <p><button type='submit'>Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    # 从request对象获取表单内容
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password!</h3>'


if __name__ == '__main__':
    app.run()

# 使用mvc模式使用flask框架

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    # 从request对象获取表单内容
    if username == 'admin' and password == 'password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password!', username=username)


if __name__ == '__main__':
    app.run()
