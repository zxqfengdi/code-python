# -*- coding:utf-8 -*-

"""
Name: 运算符.py
Author: fengdi
Datetime: 11:35 2019/3/26 
Description: 主要介绍python运算符相关内容

"""

# 算术运算符：+ - * / // % **（用来执行算术运算）
# 比较运算符：== != > >= < <= （用来进行比较运算及条件测试等）

num01 = num02 = 10
num03 = 20

print(num01 == num02, num01 != num02, num03 > num02, num03 >= num02, num03 < num02, num02 <= num03)

# 赋值运算符：= += -= *= /= %= **= //=（主要用来赋值运算）

# 位运算符：&（按位与）、 |（按位或）、 ^（按位异或:当两对应的二进位相异时，结果为1，否则为0）、 ~ （按位取反）、<<（左移）、 >>（右移）
# 位运算符主要对二进制数进行相关运算

a = 60   # 二进制表示：0011 1100
b = 13   # 二进制表示：0000 1101
c = 0

print(a & b)
print(a | b)
print(a ^ b)
print(~ a)
print(a << 2)
print(b >> 2)

# 逻辑运算符：and（逻辑与） or（逻辑或） not（逻辑非） 用来进行逻辑判断

# 成员运算符：in、not in 进行成员检查

# 身份运算符： is（表示同一对象，id相同） 、is not（表示不为同一对象）

str1 = 'hello'
str2 = str1
str3 = str1[:]

print(str1 is str2)
print(str1 is str3)

