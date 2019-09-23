# -*- coding:utf-8 -*-

"""
Name: 闭包装饰器.py
Author: fengdi
Datetime: 18:17 2019-07-16
Description:

"""


# 闭包

def out():
    """
    函数返回一个内部函数，内部函数引用了外部函数的参数或变量，
    则内部函数及引用的变量称为闭包
    :return:返回值为内部函数
    """
    num = 10

    def inner():
        print("num = %d" % num)

    return inner


ret = out()
ret()


def out():
    """
    闭包内部引用了外部函数的参数和变量，若要进行修改使用nonlocal关键字
    :return: 返回值为内部函数
    """
    num = 10

    def inner():
        nonlocal num
        num += 10
        print("修改过后num = %d" % num)

    return inner


ret = out()
ret()


# 装饰器：在不更改原函数定义的情况下给原函数增加额外功能
def decorator(func):

    def inner():
        print("------添加额外功能---------")
        func()

    return inner


def test1():
    print("---------test1---------")


test1 = decorator(test1)  # 对test1函数进行装饰
test1()


# @语法糖装饰
def decorator(func):

    def inner():
        print("--------添加额外功能----------")
        func()

    return inner


@decorator
def test1():
    print("---------test1---------")


test1()


# @装饰器在执行到时已经对原函数进行装饰
def decorator(func):
    print("对test1函数进行装饰")

    def inner():
        print("--------添加额外功能----------")
        func()

    return inner


@decorator
def test1():
    print("---------test1---------")


test1()


# 装饰无参数无返回值的函数
def decorator(func):
    print("对test1函数进行装饰")

    def inner():
        print("--------添加额外功能----------")
        func()

    return inner


@decorator
def test1():
    print("---------test1---------")


test1()


# 装饰无参数有返回值的函数
def decorator(func):

    def inner():
        print("添加额外功能")
        return func()

    return inner


@decorator
def test1():
    return "hello world!"


ret = test1()
print(ret)


# 装饰有参数无返回值的函数
def decorator(func):

    def inner(num):
        print("额外功能")
        func(num)
    return inner


@decorator
def test1(num):
    print("num = %d" % num)


test1(10)


# 装饰有参数有返回值的函数
def decorator(func):

    def inner(num):
        print("额外功能")
        return func(num)

    return inner


@decorator
def test1(num):
    return "num = %d" % num


ret = test1(10)
print(ret)


# 通用装饰器
def decorator(func):

    def inner(*args, **kwargs):
        print("添加额外功能")
        return func(*args, **kwargs)

    return inner


@decorator
def test1(num, *args, **kwargs):
    print("num = %d" % num)
    return args, kwargs


ret = test1(20)
print(ret)

ret = test1(20, 30, 40)
print(ret)

ret = test1(20, 30, 40, name="fengdi")
print(ret)


# 多个装饰器装饰一个函数
def decorator1(func):
    print("装饰器1开始装饰")

    def inner():
        print("----------装饰器1------------")
        func()
    return inner


def decorator2(func):
    print("装饰器2开始装饰")

    def inner():
        print("----------装饰器2------------")
        func()
    return inner


@decorator1
@decorator2
def test1():
    print("-----------test1-----------")


test1()


# 有参数的装饰器：作用在于返回不同类型的装饰器


def outer(num):

    def wrapper(func):

        def inner():
            print("权限验证%d" % num)
            func()

        return inner

    return wrapper


@outer(1)
def test1():
    print("---------test1---------")


@outer(2)
def test2():
    print("---------test2---------")


test1()
test2()
