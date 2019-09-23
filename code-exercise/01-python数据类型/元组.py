# -*- coding:utf-8 -*-

"""
Name: 元组.py
Author: fengdi
Datetime: 17:59 2019/3/25 
Description: 主要介绍元组（不可变对象）的表示、常用操作即常用方法。

"""

# 元组表示：使用()表示，内部可包含任意类型。tuple()函数可将其他序列类型转换为元组类型

list01 = ['hello', 'world', 'python', 'java']
tuple01 = ('hello', 'python', 'php', 15, ['hello', 'python'])
tuple02 = tuple(list01)   # tuple()函数转化其他序列类型为元组
tuple03 = ('hello')
tuple04 = ('hello', )     # 元组内只有一个元素需要加逗号

print(type(tuple01), tuple01)
print(type(tuple02), tuple02)
print(type(tuple03), tuple03)
print(type(tuple04), tuple04)

# 常用操作：索引、分片、加、乘、成员检查、长度、最大值、最小值（序列类型通用操作）

print(tuple01[0], tuple01[-1])  # 根据索引打印对应元素
print(tuple01[:2], tuple01[-2:])  # 根据索引对元组进行分片
print(tuple01 + tuple04)   # 元组相加
print(tuple04 * 3)   # 元组乘法
print('hello' in tuple01)   # 成员检查
print(len(tuple01))    # 元组长度
print(max(tuple02), min(tuple02))  # 元组最大值、最小值

# 常用方法

print(dir(tuple))   # 打印元组所有属性及方法

tuple05 = tuple03 * 4
print(tuple05.count('hello'))   # 返回给定元素的统计值
print(tuple05.index('hello'))   # 返回给定元素的第一个索引值
