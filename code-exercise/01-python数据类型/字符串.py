# -*- coding:utf-8 -*-

"""
Name: 字符串.py
Author: fengdi
Datetime: 9:01 2019/3/25 
Description: 主要介绍字符串（不可变对象）的表示方法、相关操作、格式化输出及常用方法等内容。

"""

# 字符串表示方法：单引号、双引号、转义字符、原始字符串

str1 = 'Fengdi tell me that:"Everything is possible!"'
print(type(str1))
print(str1)

str2 = "She's a beautiful girl!\n"
print(type(str2))
print(str2)

str3 = "This is a special char:\t \n."
print(type(str3))
print(str3)

str4 = r"I am a original string.\n"
str5 = R"I am a original string.\t"
print(type(str4))
print(type(str5))
print(str4)
print(str5)

# 字符串相关内置函数：repr() chr() ord() len()
# repr(): 返回包含一个对象的可打印表示形式的字符串
print(repr(10), type(repr(10)))

# chr(): 将数字转换为ASCII码中对应的字符
print(chr(97))

# ord()：将字符转换为对应ASCII数字
print(ord('a'))

# len()：获取字符串长度
print(len('hello world'))

# 字符串相关操作：索引、分片、加、乘、成员检查、长度、最大值、最小值（序列类型通用操作）

print(str2[0])   # 打印索引为0的字符
print(str2[6])   # 打印索引为6的字符
print(str2[-1])  # 打印倒数第一个字符（负值索引从-1开始）

print(str2[0:5])   # 打印索引0-4的字符串(不包括最后索引)
print(str2[-5:])   # 打印索引-5到末尾的字符串（省略取到字符串末尾）

print(str2 + ' ' + str4)   # 字符串相加即连接

print(str2 * 2)            # 字符串乘以数字即重复输出

print('girl' in str2)      # 成员检查即确认子字符串是否存在于原字符串中：返回值为布尔值（True  False）
print('boy' not in str2)

print(len(str2))           # len()：内置函数，打印字符串长度
print(len(str3))

print(max(str2))           # 打印字符串中的最大字符：按照ASCII码表排列
print(min(str2))
print(max(str1, str2))     # 比较两个字符串的大小，按照ASCII码表一一对比
print(min(str1, str2))

# 字符串输入（input、eval(input)）及格式化输出（%s占位符、.format方法）

name = input("Please enter your name:")     # 从标准输入（键盘）接收字符串赋值给变量name
print(type(name))
print(name)

name = eval(input("Please enter something:"))   # 从标准输入接受一个原始输入即输入类型就是变量name类型
print(type(name))
print(name)

language1 = 'python'
language2 = 'java'

print("My favorite language is %s.Do you like %s?" % (language1, language2))   # 使用%s作为占位符进行输出

print("My favorite language is {}.Do you like {}?".format(language1, language2))  # .format()方法使用{}作为占位符
print("My favorite language is {1}.Do you like {0}?".format(language1, language2))
print("My favorite language is {language1}.Do you like {language2}?".format(language1="python", language2="java"))


# 字符串常用方法：分割字符串、去掉空格、大小写、查找子串索引、替换及统计字串出现次数等

print(dir(str))

str6 = "Hello fengdi! my name is yuxi."
str7 = " Hello world! "

str6_list = str6.split()    # split()方法返回以特定分隔符分割的字符串列表（默认为空白符）
print(type(str6_list))
print(str6_list)

print(str7.strip())         # 去掉字符串两端空白（lstrip()、rstrip()）
print(str7.lstrip())
print(str7.rstrip())

print(str7.upper())         # 字符串大写（lower()、title()、isupper()、islower()）
print(str7.lower())
print(str7.title())
print(str7.islower())  # 布尔值
print(str7.isupper())  # 布尔值

print(str7.find('world'))   # 返回子字符串的最小索引，未找到返回-1
print(str7.index('word'))  # 返回子字符串的最小索引，未找到抛出异常

print(str7.replace('world', 'python'))   # 返回一个字串替换后的字符串副本

print(str7.count('hello'))     # 统计字串出现的次数

