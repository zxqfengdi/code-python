# -*- coding:utf-8 -*-

"""
Name: 函数.py
Author: fengdi
Datetime: 16:52 2019/5/7 
Description: 主要介绍python中函数的定义、调用及函数参数等相关问题。

"""

# 函数定义：使用def关键字定义函数（形式：def func_name(参数列表):）


def multi_table():
    """打印九九乘法表"""   # 函数文档字符串

    for column in range(1, 10):
        row = 1

        while row <= column:
            print('%d * %d = %d' % (row, column, row * column), end='   ')
            row += 1

        print('\n')

# 函数参数
# 位置实参：位置参数基于顺序传递


def info01(name, language):
    """打印相关信息"""

    print('my name is %s. my favorite language is %s.' % (name, language))

# 默认参数值：函数定义时给形参默认值，函数调用若传递参数使用被传参数，未传参使用默认参数值


def info02(name, language='go'):
    """打印相关信息"""

    print('my name is %s. my favorite language is %s.' % (name, language))

# 关键字实参:函数调用使用键值对形式传入参数，可以不考虑顺序


def info03(name, language):
    """打印相关信息"""

    print('my name is %s. my favorite language is %s.' % (name, language))

# 收集参数
# *name:会创建一个名字为name的元组，收集处位置参数之外的所有参数


def info04(name, *languages):
    """print some info"""

    print('my name is %s.' % name)

    for language in languages:
        print('my favorite language is %s.' % language)


# **keyword:创建一个名字为keyword的字典，收集多余的关键字参数


def print_info(name, **keyword):
    """print some info"""

    print('my name is %s.' % name)

    for name, language in keyword.items():
        print("%s's favorite language is %s." % (name, language))

# 当多个参数位于元组或字典中时，可使用*或**拆分参数列表


def nums(a, b, c):
    print(a + b + c)


def infos(name, language):
    print('my name is %s. my favorite language is %s.' % (name, language))


if __name__ == '__main__':
    print(multi_table.__doc__)
    multi_table()
    print(info01.__doc__)
    info01('fengdi', 'python')
    info02('fengdi')
    info03(language='java', name='yuxi')
    info04('fengdi', 'python', 'php', 'java')
    print_info('fengdi', fengdi='python', yuxi='java')
    num = (1, 2, 3)
    nums(*num)
    info = {'name':'fengdi', 'language':'python'}
    infos(**info)
