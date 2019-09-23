# -*- coding:utf-8 -*-

"""
Name: 集合.py
Author: fengdi
Datetime: 10:47 2019/3/26 
Description: 主要介绍集合类型(元素无序性不重复性)的表示、常用方法及集合运算等。

"""

# 集合表示：集合使用{}表示，内置函数set()可进行类型转换

set01 = set()  # 空集合使用set()表示，{}表示空字典
set02 = {'name', 30, ('python', 'java')}   # set()函数默认生成的为可变集合，可变即可对集合元素进行添加删除更改等。
set03 = set(['hello', 'python', 20])       # 集合内部的元素应为不可变类型即可哈希的，可用来做字典的键
set04 = frozenset(['hello', 'python', 20])  # frozenset()默认生成不可变集合

print(type(set01), set01)
print(type(set02), set02)
print(type(set03), set03)
print(type(set04), set04)

# 常用方法：添加元素、删除元素、更新集合等

print(set03)

set03.add('java')    # add()方法：向集合中添加元素
print(set03)

set03.update(['php', 'javascript'])   # update()方法：利用可迭代对象更新集合
print(set03)

set03.remove('python')  # remove()方法：删除集合中某元素，元素不存在，抛出异常
print(set03)

set03.discard('php')   # discard()方法：删除指定元素，元素不存在，无反应
print(set03)

set03.pop()       # pop()方法：随即删除某元素，集合为空抛出异常
print(set03)

set03.clear()     # clear()方法：清空集合元素
print(set03)

# 集合运算

set05 = {'hello', 'world', 'python', 20, 30}
set06 = {'python', 'java', 'c#', 30, 40, 50, 60}

print('world' in set05)     # 元素与集合关系
print('python' in set06)

print(set05 < set06)   # <与a.issubset()方法判断一个集合是否为另一个集合子集
print(set05.issubset(set06))

print(set05 > set06)   # >与a.issuperset()方法判断一个集合是否为另一个集合超集
print(set05.issuperset(set06))

print(set05 | set06)    # |与a.union()方法计算两个集合的并集
print(set05.union(set06))

print(set05 & set06)    # &与a.intersection()方法计算两个集合的交集
print(set05.intersection(set06))

print(set05 - set06)    # -与a.difference()方法计算两个集合的差集
print(set05.difference(set06))