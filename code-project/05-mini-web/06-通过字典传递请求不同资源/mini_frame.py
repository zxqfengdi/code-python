# -*- coding:utf-8 -*-

"""
Name: mini_frame.py
Author: fengdi
Datetime: 09:39 2019-07-16
Description:

"""


def index():
    return "这是主页"


def login():
    return "这是登录页面"


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    file_name = environ["file_info"]

    if file_name == "/index.py":
        return index()
    elif file_name == "/login.py":
        return login()
    else:
        return 'Hello World! 我爱你中国！！！'
