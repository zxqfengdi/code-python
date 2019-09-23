# -*- coding:utf-8 -*-

"""
Name: 异常.py
Author: fengdi
Datetime: 15:56 2019/5/7 
Description: 主要介绍python中错误和异常的处理

"""

# 异常处理：一般使用try.....except....的形式捕获并处理异常

try:
    x = 10 / 0
    print('x:', x)
except ZeroDivisionError as e:   # 捕获除数为0异常
    print('Error:', e)           # 异常处理语句

print('Hello world!')

# 可使用多个except语句捕获多种异常但只能执行一个（except不仅捕获该类异常还捕获子类异常）

try:
    x = eval(input('Enter x:'))
    y = eval(input('Enter y:'))
    z = x / y
except ZeroDivisionError as e:
    print('Error:', e)
except TypeError as e:
    print('Error:', e)

print('Hello world!')

# 捕获未知异常：BaseException是所有异常类的基类，可使用BaseException捕获未知异常

try:
    x = eval(input('Enter x:'))
    y = eval(input('Enter y:'))
    z = x / y
except ZeroDivisionError as e:
    print('Error:', e)
except TypeError as e:
    print('Error:', e)
except BaseException as e:
    print('BaseException:', e)

print('Hello world!')

# else子句：没有异常发生时执行else子句

try:
    x = eval(input('Enter x:'))
    y = eval(input('Enter y:'))
    z = x / y
except ZeroDivisionError as e:
    print('Error:', e)
except TypeError as e:
    print('Error:', e)
except BaseException as e:
    print('BaseException:', e)
else:
    print('Operate succeed!')

print('Hello world!')

# finally子句：不管异常是否发生均执行finally子句

try:
    x = eval(input('Enter x:'))
    y = eval(input('Enter y:'))
    z = x / y
except ZeroDivisionError as e:
    print('Error:', e)
except TypeError as e:
    print('Error:', e)
except BaseException as e:
    print('BaseException:', e)
else:
    print('Operate succeed!')
finally:
    print('done!')

# raise()：手动抛出异常，默认抛出当前异常的实例（也可以自定义类）


class FooError(ValueError):
    pass


try:
    x = eval(input('Enter x:'))
    y = eval(input('Enter y:'))
    z = x / y
except ZeroDivisionError as e:
    print('Error:', e)
    raise FooError('invalid value')
