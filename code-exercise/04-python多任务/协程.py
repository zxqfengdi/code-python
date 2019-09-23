# -*- coding:utf-8 -*-

"""
Name: 协程.py
Author: fengdi
Datetime: 16:30 2019-07-16
Description:

"""
import time
import greenlet
import gevent

# 协程：更加轻量级


# greenlet实现协程


def test1():
    while True:
        print('----test1-----')
        t2.switch()
        time.sleep(0.5)


def test2():
    while True:
        print('----test2-----')
        t1.switch()
        time.sleep(0.5)


t1 = greenlet(test1)
t2 = greenlet(test2)

t1.switch()


# gevent实现协程


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)

        gevent.sleep(0.5)


g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)

g1.join()
g2.join()
g3.join()