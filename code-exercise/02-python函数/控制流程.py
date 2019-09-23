# -*- coding:utf-8 -*-

"""
Name: 控制流程.py
Author: fengdi
Datetime: 14:59 2019/3/26 
Description: 主要介绍python中的常用语句：模块导入、赋值语句、条件语句、循环语句等。

"""

# 模块导入语句：python使用import 来进行模块及模块内容的导入（as设置别名简化语言）
# import module_name    导入整个模块
# from somemodule import somefuction    从某个模块导入某函数
# from somemodule import function01, function02     从某模块导入多个函数
# from somemodule import *      导入模块的所有函数

# 赋值语句：python支持多种赋值方式：链式赋值、序列解包赋值等

a = b = c = 20  # 链式赋值
print(a, b, c)

d, e = 20, 30   # 元组解包赋值
print(d, e)

# 条件语句：if--elif--else结构

# 单if语句

num01, num02 = 20, 30

if num02 > num01:
    print("The num02 is bigger than num01.")

# if-else语句

num01, num02 = 30, 20

if num02 > num01:
    print("The num02 is bigger than num01.")
else:
    print("The num02 is not bigger than num01.")

# if-elif-else语句

num01, num02 = 20, 20

if num02 > num01:
    print("The num02 is bigger than num01.")
elif num02 == num01:
    print("num02 == num01.")
else:
    print("The num02 is lower than num01.")

# 三元操作符

num01, num02 = 30, 20

# print("The num01 is bigger than num02.") if num01 > num02 else print("The num02 is not bigger than num01.")


# 循环语句

# for循环：一般与range()函数、序列类型、字典及可迭代对象结合使用

for num in range(1, 20, 2):
    print(num)

my_list = [10, 20, 30, 40]
for x in my_list:
    print(x)

my_dict = {'name':'fengdi', 'age':24, 'language':'python'}
for dict_key, dict_value in my_dict.items():
    print(dict_key, dict_value)

# 特殊函数：zip()函数、enumerate()函数

# zip()函数：接收多个可迭代对象，将其组合为列表形式，返回一个迭代器对象

my_list = [10, 20, 30, 40]
my_tuple = ('hello', 'world', 'python')
new_obj = zip(my_list, my_tuple)
print(type(new_obj), new_obj)

# enumerate()函数：接收可迭代对象作为参数，将其索引及对应值组合在一起，返回一个迭代器对象

enum_obj = enumerate(my_tuple)
print(type(enum_obj), enum_obj)

# while循环：循环中语句应可以改变循环条件，避免成为死循环

num = 1
sum = 0

while num <= 100:
    sum += num
    num += 1

print(sum)

for x in 'hello':
    if x == 'e':
        break     # 跳出整个循环
    print(x)

for x in 'hello':
    if x == 'e':
        continue   # 跳出当前循环，进行下一轮循环
    print(x)


# 循环语句和else语句结合使用：用于循环结束后执行相关操作

str_lists = ['hello', 'world', 'python', 'java']

for str_list in str_lists:
    print(str_list)
else:
    print('All strings have been printed.')

# pass语句：占位作用，保证程序完整可运行


def my_func():
    pass

