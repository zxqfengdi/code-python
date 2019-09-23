# -*- coding:utf-8 -*-

"""
Name: 函数式编程.py
Author: fengdi
Datetime: 8:59 2019/5/8 
Description: 主要介绍函数式编程的相关内容：高阶函数、闭包、匿名函数、装饰器等。

"""

from functools import reduce

# 函数式编程：
# 变量可指向函数，即可将函数名作为参数传入另一个函数


def print_hello():
    """print hello world"""
    print('hello world')

# 高阶函数：一个函数接收另一个函数作为参数，即为高阶函数


def func_test(func, x):
    return func(x)


def square(num_list):
    for x in range(num_list):
        print(x ** 2)

# 内置高阶函数:map() reduce() filter() sorted()
# map()函数：接收一个函数和一个可迭代对象作为参数，将函数作用于每一个参数并返回一个迭代器对象


def factorial(x):
    """计算阶乘"""

    result = 1
    while x >= 1:
        result = result * x
        x -= 1
    return result

# reduce函数：接收一个函数和一个可迭代对象作为参数，该函数接收可迭代对象的前两个元素作为参数执行，将结果和第三个参数作为参数继续执行


def multi(x, y):
    """计算两数之和"""
    return x + y

# filter()函数：接收一个函数和一个可迭代对象作为参数，将函数作用于可迭代对象的每一个元素，对结果（True False）进行筛选，返回类型为迭代器


def odd(x):
    return x % 2

# sorted()函数：接受一个可迭代对象和一个函数作为参数，用于对可迭代对象进行按条件排序


def my_abs(x):
    """计算绝对值"""

    return abs(x)

# 闭包：一个函数返回一个内部函数，其内部函数引用了外部函数的相关变量和参数，则返回的内部函数称为闭包。
# 应用场景：可根据不同的参数生成不同的返回函数


def make_add(x, y):
    """define a closure function"""

    def add():
        return x + y
    return add

# 匿名函数：lambda函数  形式：lambda 参数:表达式  适用于创建临时性的小巧的函数

lambda_func = lambda x : x ** 2

# 装饰器：在不改变原有函数的定义和调用过程情况下，给函数增加新的功能。
# （本质上是个高阶函数，接收被装饰函数作为参数，返回一个新的内部函数，内部函数增加原有函数的功能）


def my_func01():
    """print A"""
    print('AAAA')


def decorator01(func):
    """define a decorator"""
    def inner():
        print('--------')
        func()
    # 闭包：内部函数使用外部函数的参数
    return inner

# 装饰器语法糖


def decorator02(func):
    """define a decorator"""
    def inner():
        print('--------')
        func()
    # 闭包：内部函数使用外部函数的参数
    return inner


@decorator02
def my_func02():
    """print A"""
    print('AAAA')


if __name__ == '__main__':
    print_hello()   # 函数调用
    my_print = print_hello   # 将变量指向函数
    print(type(my_print))    # 可以看出变量名指向函数名后也为函数
    my_print()               # 使用变量调用函数

    func_test(square, 5)     # 将函数名square作为参数传递给形参func

    my_list = list(range(1, 5))
    map_result = map(factorial, my_list)  # 接收一个函数和可迭代对象作为参数，返回类型为迭代器
    print(type(map_result))
    print(list(map_result))

    my_list = [1, 2, 3, 8, 62]
    reduce_result = reduce(multi, my_list)  # 接收一个函数和一个可迭代对象作为参数
    print(reduce_result)
    print(sum(my_list))

    my_list = list(range(1, 30))
    filter_result = filter(odd, my_list)  # 接收一个函数和可迭代对象作为参数，返回类型为迭代器
    print(list(filter_result))

    my_list = [-6, 25, 7, -65, -9, 28]
    sorted_result = sorted(my_list, key=my_abs)  # 接受一个可迭代对象和一个函数作为参数，用于对可迭代对象进行按条件排序
    print(type(sorted_result))
    print(sorted_result)

    make_add_return = make_add(5, 6)
    print(type(make_add_return))
    print(make_add_return())

    print(lambda_func)
    lambda_result = lambda_func(5)
    print(lambda_result)

    my_func01 = decorator01(my_func01)
    my_func01()

    my_func02()

