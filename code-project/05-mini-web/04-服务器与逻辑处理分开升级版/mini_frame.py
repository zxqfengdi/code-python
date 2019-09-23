# -*- coding:utf-8 -*-

"""
Name: mini_frame.py
Author: fengdi
Datetime: 17:22 2019-07-15
Description:

"""
import time


def login():
    response_body = "welcome to our website......  time:%s" % time.ctime()
    return response_body


def register():
    response_body = "welcome to register our website......  time:%s" % time.ctime()
    return response_body


def application(file_name):
    if file_name == '/login.py':
        return login()
    elif file_name == '/register.py':
        return register()
    else:
        return "not found page......"
