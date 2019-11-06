# -*- coding:utf-8 -*-

"""
Name: mini_frame.py
Author: fengdi
Datetime: 17:09 2019-07-15
Description: HTTP服务器与逻辑处理分开

"""
import time


def login():
    response_body = "welcome to my website......  time:%s" % time.ctime()
    return response_body
