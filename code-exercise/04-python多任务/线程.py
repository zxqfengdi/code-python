# -*- coding:utf-8 -*-

"""
Name: 线程.py
Author: fengdi
Datetime: 16:29 2019-07-16
Description: 多线程

"""

import time
import threading

# 线程：多任务可通过多线程实现。一个程序默认只有一个线程即主线程，可在主线程内创建子线程。多个子线程执行顺序不一定，由cpu调度决定。可通过延时操作来控制线程执行顺序（谁先执行后面主线程延时）
# 方法一：使用threading.Thread()类创建线程实例实现多线程


def AA():
    for x in range(10):
        print("-----AA-----")
        time.sleep(1)


def BB():
    for x in range(5):
        print("-----BB-----")
        time.sleep(0.5)


t1 = threading.Thread(target=AA)
t2 = threading.Thread(target=BB)
t1.start()
t2.start()
time.sleep(2)
print('hello world!')

# 方法二：继承threading.Thread()类，重写__init__和run()方法


class MyThread(threading.Thread):

    def __init__(self, num, sleep_time, info):
        super().__init__()
        self.num = num
        self.sleep_time = sleep_time
        self.info = info

    def run(self):
        for x in range(self.num):
            print("----%s----" % self.info)
            time.sleep(self.sleep_time)


t1 = MyThread(10, 1, 'AA')
t2 = MyThread(5, 0.5, 'BB')
t1.start()
t2.start()
time.sleep(2)
print('hello world!')


# 互斥锁：一个进程内的多个线程共享该进程的内存，即全局变量。当多个进程对同一变量进行修改会导致资源竞争问题。
# 可使用互斥锁来保证同时只有一个线程执行并获取变量，尽量减少加锁的代码。


g_num = 0


def AA():
    global g_num
    for x in range(1000000):
        g_num += 1
    print("g_num:", g_num)


def BB():
    global g_num
    for x in range(1000000):
        g_num += 1
    print("g_num:", g_num)


t1 = threading.Thread(target=AA)
t2 = threading.Thread(target=BB)
t1.start()
t2.start()
time.sleep(0.1)
print('hello world!')

lock = threading.Lock()  # 获得互斥锁
g_num = 0


def AA():
    lock.acquire()  # 上锁
    global g_num
    for x in range(1000000):
        g_num += 1
    print("g_num:", g_num)
    lock.release()  # 释放锁


def BB():
    lock.acquire()
    global g_num
    for x in range(1000000):
        g_num += 1
    print("g_num:", g_num)
    lock.release()


t1 = threading.Thread(target=AA)
t2 = threading.Thread(target=BB)
t1.start()
t2.start()
time.sleep(0.5)
print('主线程:%d' % g_num)