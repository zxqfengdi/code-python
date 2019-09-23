# -*- coding:utf-8 -*-

"""
Name: 正则表达式.py
Author: fengdi
Datetime: 8:18 2019/5/13 
Description:主要介绍python正则表达式的相关内容。

"""

import re

# 正则表达式：是匹配文本字段的模式。内置模块re提供对正则表达式的支持。正则表达式有两种使用方法：1. 预编译表达式生成pattern，使用其方法进行匹配 2. 将表达式传入re模块的函数进行匹配
# 匹配过程如下：1. 使用re.compile()函数将构造的正则表达式编译为pattern对象（模式） 2. 通过pattern对象提供的方法对文本进行匹配，返回一个match对象 3. 利用match对象的方法获得匹配的数据信息

# pattern.match()方法：match(str, pos, endpos)  str:要匹配的文本 pos和endpos:匹配的范围即起始和结束位置
# 属于单次匹配，即找到一个结果就返回。匹配成功返回一个match对象，否则返回None.
pattern = re.compile(r'\d+')    # 匹配数字，大于1个
print(pattern)

m = pattern.match('565yuxi216516python')
p = pattern.match('fengdi979yuxi1321535python', 6, 10)    # 指定pattern匹配的范围
n = pattern.match('fengdi')

print(m, p, n)

# 调用匹配成功返回match对象的相关方法，获得匹配结果信息
print(p.group())        # 返回匹配的结果
print(p.start())        # 返回匹配结果在原文本中的起始位置
print(p.end())          # 返回匹配结果在原文本中的结束位置
print(p.span())         # 返回匹配结果在原文本中的索引范围

# pattern.search()方法：搜索整个字符串，匹配成功一个就返回

m = pattern.search('one123two456fengdi')   # 返回为match对象
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())

# pattern.findall()方法：寻找原文本内所有匹配成功的结果，以列表形式返回

m = pattern.findall('one123two456fengdi')   # 返回类型为列表
print(m)

# pattern.finditer()方法：搜索整个文本，返回一个包含顺序匹配结果的迭代器

m = pattern.finditer('one123two456fengdi')
print(m, type(m))
print(list(m))

for result in m:
    print(result.group())

# pattern.split()方法：按照给定的模式将文本分割后返回列表

pattern = re.compile(r'[\s,;]+')

m = pattern.split('a,b;; c  d')
print(type(m), m)

# pattern.sub()方法：使用指定字符串或函数返回的字符串替换pattern匹配到的字符串

pattern = re.compile(r'(\w+) (\w+)')
word = 'hello 123, hello 456'


def func(word):
    return 'hi' + ' ' + word.group(1)  # 返回一个字符串用于替换


print(pattern.sub(r'hello world', word))  # 使用字符串替换
print(pattern.sub(r'\2 \1', word))  # 引用匹配到的子串的分组进行替换
print(pattern.sub(func, word))  # 使用函数返回一个字符串用于替换
print(pattern.sub(func, word, 1))   # 指定替换的次数

# pattern.subn()：使用指定字符串或函数返回的字符串替换pattern匹配到的字符串，返回一个元组(替换后的字符串，替换的次数)

pattern = re.compile(r'(\w+) (\w+)')
word = 'hello 123, hello 456'


def func(word):
    return 'hi' + ' ' + word.group(1)  # 返回一个字符串用于替换


print(pattern.subn(r'hello world', word))  # 使用字符串替换
print(pattern.subn(r'\2 \1', word))  # 引用匹配到的子串的分组进行替换
print(pattern.subn(func, word))  # 使用函数返回一个字符串用于替换
print(pattern.subn(func, word, 1))   # 指定替换的次数

# match()函数：格式：match(pattern, str),pattern为正则表达式的字符串形式

result01 = re.match(r'\d+', 'one12two34three56')
result02 = re.match(r'\d+', '123onetwo456')

print(type(result01), type(result02))
print(result02.group())

# search()函数：格式：re.search(pattern, str)

result = re.search(r'\d+', 'one123two456three')

if result:
    print('result:', result.group())

# findall()函数：格式：re.findall(pattern, str)

result = re.findall(r'\d+', 'one123two567three890')
if result:
    print(type(result),result)

# findiner()函数：格式：re.finditer(pattern, str)

result = re.finditer(r'\d+', 'one123two567three890')
print(type(result))

# sub()函数：格式：re.sub(pattern, repl, str)

result01 = re.sub(r'(\w+) (\w+)', r'hello world', 'hello 123, hello 456')
result02 = re.sub(r'(\w+) (\w+)', r'\2 \1', 'hello 123, hello 456')

print(result01)
print(result02)

# subn()函数：格式：re.subn(pattern, repl, str)

result01 = re.subn(r'(\w+) (\w+)', r'hello world', 'hello 123, hello 456')
result02 = re.subn(r'(\w+) (\w+)', r'\2 \1', 'hello 123, hello 456')

print(result01)
print(result02)


# 贪婪匹配：python中正则表达式默认贪婪匹配（尽可能匹配较多的字符）。即匹配到第一个结果时，会尝试向右匹配，查看是否还有更长的匹配结果。加?变为非贪婪匹配。

word = 'aa<div>test1</div>bb<div>test2</div>cc'

result = re.findall(r'<div>.+</div>', word)
print(result)

result = re.findall(r'<div>.+?</div>', word)
print(result)
