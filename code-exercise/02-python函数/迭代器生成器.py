# -*- coding:utf-8 -*-

"""
Name: 迭代器生成器.py
Author: fengdi
Datetime: 19:16 2019/5/7 
Description:主要介绍生成器和迭代器的相关内容

"""

from collections import Iterable

# 迭代器iterator：可被next()方法调用或具有__next__()方法，不断生成下一个值的对象（表示一个惰性计算序列）
# 判断对象是否可以迭代

my_str = 'hello'
my_list = ['hello', 1, 50]

print(isinstance(my_str, Iterable))
print(isinstance(my_list, Iterable))

# iter()函数可将可迭代对象转变为迭代器对象(使用next()函数不断获取下一个值)

iterator_obj = iter(my_list)
print(type(iterator_obj))

for x in range(3):
    print(next(iterator_obj))

# for循环迭代的后台机制：使用iter()函数将可迭代对象转变为迭代器，不断调用next()方法获取下一个值

# 自定义类实现迭代器（斐波那契数列）


class Fib(object):
    """斐波那契数列"""

    def __init__(self, num):
        self.num = num
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.num:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            return ret
        else:
            raise StopIteration


fib = Fib(10)
for num in fib:
    print(num)

# 生成器generator:生成器自带迭代器协议，自身可迭代；提供延迟操作，内存占用少；生成器表达式类似于列表解析式

num = [x for x in range(10)]
print(type(num), num)

iterator_num = (x for x in range(10))  # 生成器表达式
print(type(iterator_num))

print(isinstance(iterator_num, Iterable))  # 生成器本身可迭代

# 生成器函数：常规函数定义，使用yield语句而不是return语句返回结果


def generator_fuc(num):
    """定义一个生成器函数"""

    for x in range(num):
        yield x


my_num = generator_fuc(10)
print(type(my_num))

for num in my_num:
    print(num)
