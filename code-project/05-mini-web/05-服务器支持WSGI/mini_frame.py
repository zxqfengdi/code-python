# -*- coding:utf-8 -*-

"""
Name: mini_frame.py
Author: fengdi
Datetime: 19:10 2019-07-15
Description:

"""


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    return 'Hello World! 我爱你中国！！！'


