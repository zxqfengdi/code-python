# -*- coding:utf-8 -*-

"""
Name: 字典.py
Author: fengdi
Datetime: 18:31 2019/3/25 
Description: 主要介绍字典类型(无序性)的表示方法、基本操作及常用方法。

"""
import copy

# 字典表示方法：字典使用{}表示，由键值对组成。键不可重复且只能由不可变类型(字符串、元组)组成，值可为任意类型可重复。

dict1 = {}   # 空字典
dict2 = {'name': "fengdi", "language": "python", "city": "wuhan", "num_list": [20, 30, 40]}   # 键值对构造字典
dict3 = dict(name="fengdi", age=23, language="java")    # 关键字参数构造字典
dict4 = dict([("name", "fengdi"), ("age", 23), ("language", "php")])

print(type(dict1), dict1)
print(type(dict2), dict2)
print(type(dict3), dict3)
print(type(dict4), dict4)

# 常用操作：字典长度、获取某个键对应的值、字典元素重新赋值、删除某键值对及成员检查

print(len(dict2))    # 返回字典长度即字典中键的个数

print(dict2['language'])   # dict[key]:返回字典中某个键对应的值（与序列类型相比，序列类型以索引来获取元素，字典类型以键来获取元素）

print(dict2)
dict2['city'] = "beijing"   # 使用dict[key]=""来给字典元素重新赋值(若key不存在即添加到字典中)
print(dict2)

del dict3["age"]   # 使用del语句删除字典某元素
print(dict3)

print("name" in dict2)   # 字典成员检查

# 常用方法：深浅复制、清空元素、查找键值对、删除指定键值对及更新字典等

print(dir(dict))

# 浅复制：同列表的浅复制一样，浅复制操作后整体为一个新对象；对于内部对象来说，简单类型（字符串、数字、元组）为新对象，复杂类型（列表、字典、集合）仍为引用。

copy_dict01 = {'name': "fengdi", "age": 20, "num_list": [20, 30, 40], "num_tuple": (40, 50, 60)}
copy_dict02 = copy_dict01
copy_dict03 = copy_dict01.copy()

print(id(copy_dict01), copy_dict01)
print(id(copy_dict02), copy_dict02)
print(id(copy_dict03), copy_dict03)
print('---------------------------------------------------------')

copy_dict01['name'] = 'yuxi'
print(id(copy_dict01), copy_dict01)
print(id(copy_dict02), copy_dict02)
print(id(copy_dict03), copy_dict03)
print('---------------------------------------------------------')

copy_dict01['age'] = 30
print(id(copy_dict01), copy_dict01)
print(id(copy_dict02), copy_dict02)
print(id(copy_dict03), copy_dict03)
print('---------------------------------------------------------')

copy_dict01['num_list'][0] = 50
print(id(copy_dict01), copy_dict01)
print(id(copy_dict02), copy_dict02)
print(id(copy_dict03), copy_dict03)
print('---------------------------------------------------------')

# 深复制：同列表的深复制一样，深复制操作后整体为一个新对象；对于内部对象来说，也均为新对象。

copy_dict04 = {'name': "fengdi", "age": 20, "num_list": [20, 30, 40], "num_tuple": (40, 50, 60)}
copy_dict05 = copy.deepcopy(copy_dict04)

print(id(copy_dict04), copy_dict04)
print(id(copy_dict05), copy_dict05)
print('---------------------------------------------------------')

copy_dict04['name'] = 'yuxi'
print(id(copy_dict04), copy_dict04)
print(id(copy_dict05), copy_dict05)
print('---------------------------------------------------------')

copy_dict04['age'] = 30
print(id(copy_dict04), copy_dict04)
print(id(copy_dict05), copy_dict05)
print('---------------------------------------------------------')

copy_dict04['num_list'][0] = 50
print(id(copy_dict04), copy_dict04)
print(id(copy_dict05), copy_dict05)
print('---------------------------------------------------------')

dict5 = {'name': "fengdi", "age": 20, "num_list": [20, 30, 40], "num_tuple": (40, 50, 60)}

print(dict5.setdefault('name'))     # setdefault()方法：查找某键的值，若存在返回对应值；键不存在，可设置对应值并返回设置的对应值并添加到字典中，未设置对应值则默认为none，并添加到字典中
print(dict5.setdefault('language'), dict5)
print(dict5.setdefault('city', 'wuhan'), dict5)

print(dict5)
print(dict5.get('name'))            # get()方法：查找某键的值，若存在返回对应值；键不存在，可设置对应值并返回设置的对应值，未设置对应值则默认为none（不添加到字典中）.
print(dict5.get('people'), dict5)
print(dict5.get('hobby', 'code'), dict5)

dict6 = {'name': "fengdi", "language": "python", "city": "wuhan", "num_list": [20, 30, 40]}

dict_items = dict6.items()     # 返回视图，键值对组成的列表形式，多用来遍历操作
print(type(dict_items), dict_items)
dict_keys = dict6.keys()       # 返回视图，键组成的列表形式，多用来遍历操作
print(type(dict_keys), dict_keys)
dict_values = dict6.values()   # 返回视图，值组成的列表形式，多用来遍历操作
print(type(dict_values), dict_values)

print(dict6.pop('name'), dict6)       # pop()：删除某个键对应的键值对并返回其值，键不存在可设定返回指定值，否则抛出错误
print(dict6.pop('hobby', "It's not exists."), dict6)

dict7 = {'name': "fengdi", "language": "python", "city": "wuhan", "num_list": [20, 30, 40]}
print(dict7.popitem())   # popitem()：随机删除一键值对，并以元组形式返回，字典为空，抛出异常

dict8 = {'name': "fengdi", "language": "python", "city": "wuhan", "num_list": [20, 30, 40]}
dict9 = {'hobby': 'code', 'age': 24}
iterable_obj = [('hello', 'world'), ('color', 'green')]

print(dict8)
dict8.update(dict9)   # update()：从另一个字典或可迭代对象更新字典
print(dict8)
dict8.update(iterable_obj)
print(dict8)

dict8.clear()      # clear()：清空字典元素
print(dict8)
