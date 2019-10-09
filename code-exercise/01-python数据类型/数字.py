# -*- coding:utf-8 -*-

"""
Name: 数字.py
Author: fengdi
Datetime: 15:17 2019/3/25 
Description: 主要介绍python数字类型（不可变类型）的分类、相关模块及函数等。

"""


# 数字类型:int、float、complex、Bool类型等，并可使用int()、float()、complex()、bool()进行数据类型转换

int_num = 20
float_num = 5.7
complex_num = 5 + 6j
bool_num = True

print(type(int_num))
print(type(float_num))
print(type(complex_num))
print(type(bool_num))
print(int(float_num))
print(float(int_num))
print(complex(int_num))
print(bool(int_num))

# 数字类型的算术运算：+ - * / // % **

sum_num = int_num + float_num   # 两个int类型相加和为int类型，若有一个为float类型，和为float类型
print(type(sum_num), sum_num)

sub = int_num - float_num  # 两个int类型相减差为int类型，若有一个为float类型，差为float类型
print(type(sub), sub)

multi = int_num * float_num  # 两个int类型相乘积为int类型，若有一个为float类型，积为float类型
print(type(multi), multi)

division = int_num / float_num  # python3除法操作结果默认为float类型
print(type(division), division)

exact_division = int_num // float_num   # 整除，只保留商的整数部分
print(type(exact_division), exact_division)

remainder = int_num % float_num  # 余数
print(type(remainder), remainder)

power = 5 ** 3   # 乘方
print(type(power), power)

# python数字类型常用模块：math模块、cmath模块（复数）

import math
import cmath
import random

# python常用内置函数：id()、type()、dir()、help()、abs()、round()、divmod()、floor()、bin()、hex()

print(id(int_num), id(float_num))    # id()函数返回对象的内存地址
print(type(int_num), type(float_num))  # float()函数返回对象的数据类型
print(dir(math))   # dir()函数返回给定对象的相关属性
print(dir(cmath))
help(id)   # 打印给定对象的帮助信息(交互模式)
print(abs(-100.5))   # 返回给定参数的绝对值
print(round(5.78))   # 四舍五入给定对象到指定精度
print(round(5.67589, 2))
print(divmod(5, 2))   # 返回一个元组，内部值为商和余数(x//y, x%y)
print(bin(10), type(bin(10)))  # 将数字转换为0b开头的二进制字符串形式
print(hex(234), type(hex(234)))  # 将数字转换为0x开头的十六进制字符串形式

print(math.sqrt(25))   # 开方运算
print(math.floor(5.688))  # 返回下舍整数

for x in range(10):  # 使用random模块打印伪随机数
    randint_num = random.randint(1, 100)
    print(randint_num)
