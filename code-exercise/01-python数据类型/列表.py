# -*- coding:utf-8 -*-

"""
Name: 列表.py
Author: fengdi
Datetime: 16:16 2019/3/25 
Description: 主要介绍列表（可变类型）的表示方法、常用操作、常用方法及列表解析等。

"""

import copy

# 列表使用[]来表示，为有序集合，使用索引来访问元素。list()内置函数可进行类型转换

list01 = ['hello', 'python', 'fengdi', 'java', 90]
list02 = list('Hello')
list03 = list(range(1, 10, 2))

print(type(list01), type(list02), type(list03))
print(list01)
print(list02)
print(list03)

# 常用操作:索引、分片、加、乘、成员检查、长度、最大值、最小值（序列类型通用操作）

print(list01[0], list01[-2])   # 使用索引来访问列表内元素
print(list01[0:3], list01[-3:])   # 使用索引对列表进行分片操作
print(list01 + list02)   # 两个列表相加即合并为一个列表
print(list01 * 2)   # 将列表扩展为原来的n倍
print('hello' in list01)  # 检查列表内是否包含某元素
print(len(list01), len(list02))   # 返回列表长度
print(max(list02), min(list02))   # 返回列表内的最大值、最小值

for x in list01:   # 使用for循环遍历列表元素
    print(x)


list01[0] = 'c#'    # 使用重新赋值的方法改变列表元素
print(list01)

del list01[-1]     # 使用del语句删除列表内某个元素
print(list01)

# 常用方法：添加元素、插入元素、扩展列表、统计元素出现次数、元素索引、删除指定索引元素、删除指定元素、复制、清空元素、排序及元素反转、深浅复制等。

print(dir(list))  # 打印列表的所有属性和方法

list01.append('php')   # append()方法为列表添加末尾元素，返回值为none
print(list01)

list01.extend('abs')   # extend()方法通过可迭代对象扩展列表，返回值为none
print((list01))

list01.insert(2, 'javascript')  # insert()方法向列表指定索引位置添加元素
print(list01)

print(list01.count('python'))   # 统计某元素出现的次数

print(list01.index('python'))   # 返回列表中某元素的起始索引

list01.pop(3)  # 删除指定位置的元素，无参数即删除最后一个元素，返回值即删除的元素
print(list01)

list01.remove('a')  # 移除列表中给定参数的第一个匹配值
print(list01)

list04 = list01.copy()  # 返回列表的副本，是一个新对象，内存地址不同
list05 = list01[:]      # 复制list01对象生成一个新的对象，功能同上
list06 = list01         # 直接赋值，两者指向同一对象即内存地址相同
print(id(list01), id(list04))
print(id(list01), id(list05))
print(id(list01), id(list06))
print(list04)
print(list05)
print(list06)

list06.clear()    # 清空某列表中元素
print(list06)

print(list04)
list04.sort()     # 对列表中元素进行排序(原地修改)，默认升序；设置reverse=True为降序
print(list04)
list04.sort(reverse=True)
print(list04)

list07 = sorted(list04)  # 对列表中元素进行排序，默认升序；设置reverse=True为降序（区别：生成一个副本，不改变原对象）
print(list04)
print(list07)

print(list05)
list05.reverse()     # 对列表元素进行反转
print(list05)

list08 = reversed(list05)   # 对列表元素进行反转，返回一个迭代器对象(区别：生成一个副本，不改变原对象)
print(list05)
print(list(list08))

# 列表的深浅复制
# 浅复制

copy_list01 = ['hello', 20, ['python', 'java'], {"name":"fengdi", "age":24}, ('name', 'city')]
copy_list02 = copy_list01      # 此处为赋值，内存中为直接引用
copy_list03 = copy_list01.copy()    # 列表对象自带的浅拷贝，整体对象为一个新对象，内部仍为引用
copy_list04 = copy.copy(copy_list01)    # copy模块中的浅拷贝，整体对象为一个新对象，内部仍为引用

print(id(copy_list01), copy_list01)
print(id(copy_list02), copy_list02)
print(id(copy_list03), copy_list03)
print(id(copy_list04), copy_list04)
print('------------------------------------------------------')

copy_list01[0] = 'world'    # 改变原始列表中一个字符串元素的值
print(id(copy_list01), copy_list01)
print(id(copy_list02), copy_list02)    # copy_list02为直接引用，因此会改变
print(id(copy_list03), copy_list03)    # copy_list03为新对象（备份），因此不会改变
print(id(copy_list04), copy_list04)    # copy_list04为新对象（备份），因此不会改变
print('------------------------------------------------------')

copy_list01[1] = 30
print(id(copy_list01), copy_list01)    # 此处同上
print(id(copy_list02), copy_list02)
print(id(copy_list03), copy_list03)
print(id(copy_list04), copy_list04)
print('------------------------------------------------------')

copy_list01[2][1] = 'php'
print(id(copy_list01), copy_list01)
print(id(copy_list02), copy_list02)   # copy_list02为直接引用，因此会改变
print(id(copy_list03), copy_list03)   # copy_list03整体为新对象（第一层备份），但内部复杂类型（列表、字典、集合）仍为原始对象引用，因此会改变
print(id(copy_list04), copy_list04)   # copy_list04整体为新对象（第一层备份），但内部复杂类型（列表、字典、集合）仍为原始对象引用，因此会改变
print('------------------------------------------------------')

copy_list01[3]['age'] = 25
print(id(copy_list01), copy_list01)   # 此处同上
print(id(copy_list02), copy_list02)
print(id(copy_list03), copy_list03)
print(id(copy_list04), copy_list04)
print('------------------------------------------------------')

# 深复制

copy_list05 = ['hello', 20, ['python', 'java'], {"name":"fengdi", "age":24}, ('name', 'city')]
copy_list06 = copy.deepcopy(copy_list05)   # copy模块的深层复制，整体为新对象，内部元素均为新对象（非引用）

print(id(copy_list05), copy_list05)
print(id(copy_list06), copy_list06)
print('------------------------------------------------------')

copy_list05[0] = 'world'
print(id(copy_list05), copy_list05)
print(id(copy_list06), copy_list06)   # copy模块的深层复制，整体为新对象，内部元素均为新对象（非引用），因此不会改变
print('------------------------------------------------------')

copy_list05[1] = 30
print(id(copy_list05), copy_list05)
print(id(copy_list06), copy_list06)   # copy模块的深层复制，整体为新对象，内部元素均为新对象（非引用），因此不会改变
print('------------------------------------------------------')

copy_list05[2][1] = 'php'
print(id(copy_list05), copy_list05)
print(id(copy_list06), copy_list06)   # copy模块的深层复制，整体为新对象，内部元素均为新对象（非引用），因此不会改变
print('------------------------------------------------------')

copy_list05[3]['age'] = 25
print(id(copy_list05), copy_list05)
print(id(copy_list06), copy_list06)   # copy模块的深层复制，整体为新对象，内部元素均为新对象（非引用），因此不会改变


# 列表解析：从序列中创建列表，表达式后面可跟if或者for语句来满足所需条件

obj_range = range(0, 10, 2)    # 内置函数range()接收start,stop,step三个参数来生成一个整数序列
print(type(obj_range))
print(obj_range)          # 可使用list()函数将其转化为列表 my_list = list(range(1, 10, 2))

list10 = [x for x in range(10)]
print(list10)

list11 = [x for x in range(100) if x % 5 == 0]
print(list11)

list12 = [(x, y) for x in range(3) for y in range(3)]
print(list12)

