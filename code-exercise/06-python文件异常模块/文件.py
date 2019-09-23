# -*- coding:utf-8 -*-

"""
Name: 文件.py
Author: fengdi
Datetime: 8:23 2019/5/7 
Description: 主要介绍与文件相关的操作，如文件的读写操作及对象的序列化及反序列化操作。

"""
import pickle
import json

# 文件的读操作：注意文件操作完毕应关闭文件，读操作将文件内容读入内存，不关闭文件较消耗内存

file_object01 = open('my_file.txt', 'rt')  # 使用文件名称打开文件对象（文件在当前工作目录）

print(file_object01.read())

file_object01.close()

try:                                       # 使用try....finally....语句来关闭文件
    file_object01 = open('my_file.txt', 'rt')
    print(file_object01.read())
finally:
    file_object01.close()

# with...as...语句用绝对路径打开文件，会自动调用close()方法关闭文件
with open(r'/Users/yuxi/Code/code-exercise/python基础/my_file.txt', 'rt') as file_object02:
    print(file_object02.read())

# 读取文件的多个方法：read()  readline()   readlines()

with open('my_file.txt', 'rt') as file:
    print(file.read(10))           # read(x)给定参数表示读取指定数目字符

with open('my_file.txt', 'rt') as file:
    print(file.read())           # read()未给定参数表示读取文件所有内容（大文件尽量不要使用）

with open('my_file.txt', 'rt') as file:
    print(file.tell())               # 打印文件指针当前位置
    print(file.readline())           # readline()读取一行（有两个换行，一个为文件每行最后的换行，一个为print函数的换行）
    print(file.tell())
    print(file.readline())
    print(file.tell())

with open('my_file.txt', 'rt') as file:  # 可使用readline()和while循环打印文件所有内容，需要判断末尾空行停止循环

    while True:
        line = file.readline()
        print(line)
        if not line:
            break

with open('my_file.txt', 'rt') as file:   # 文件对象本身为可迭代对象，可使用for循环进行遍历

    for line in file:
        print(line)

with open('my_file.txt', 'rt') as file:  # readlines()读取每一行内容（包括换行符），返回值为每行内容组成的列表
    line_list = file.readlines()
    print(type(line_list), line_list)

    for line in line_list:
        print(line)

# 文件的写操作：open()函数的mode参数及write()方法

with open('create_myfile.txt', 'w') as file:   # w参数：文件存在清空内容并写入，文件不存在先创建文件再进行写入（返回值为写入的字符数）
    char_num = file.write("Hello! I create a TXT file.\n")
    print(char_num)

with open('create_myfile.txt', 'a') as file:  # a参数：在文件末尾添加内容
    file.write("I add a new line after this file.\n")

# with open('create_myfile.txt', 'x') as file:  # x参数：新建文件并以写模式打开
#     file.write("I add a new line after this file.\n")

# 文件指针问题:tell() seek()

with open('my_file.txt', 'rt') as file:
    print(file.tell())  # tell()方法返回当前文件指针位置
    file.seek(5, 0)  # seek()

# 对象的序列化和反序列化:使用pickle模块实现序列化及反序列化

# 序列化：dumps()  dump() python对象转化为可存储或可传输形式（bytes格式）
num_list = [1, 2, 3, 4]

dumps_list = pickle.dumps(num_list)   # dumps()方法：将python对象序列化为Bytes格式，可存储在文件中或进行传输
print(dumps_list)

with open('dump_object.txt', 'wb') as file:
    num = file.write(dumps_list)
    print(num)

with open('dump_object.txt', 'rb') as file:
    print(file.read())

my_dict = dict(name='fengdi', age=24, hobby='coding')

with open('dump_object.txt', 'wb') as file:
    pickle.dump(my_dict, file)

with open('dump_object.txt', 'rb') as file:
    print(file.read())

# 反序列化：将bytes格式转化为python对象

with open('dump_object.txt', 'rb') as file:
    bytes_content = file.read()
    loads_object = pickle.loads(bytes_content)
    print(loads_object)

with open('dump_object.txt', 'rb') as file:
    load_object = pickle.load(file)
    print(load_object)

# python对象和json对象转换

my_dict = dict(name='fengdi', age=24, hobby='coding')

json_my_dict = json.dumps(my_dict)
print(type(json_my_dict), json_my_dict)

with open(r'F:\code-exercise\myfile.txt', 'w') as file:
    file.write(json_my_dict)

with open('/Users/yuxi/Code/code-exercise/python基础/my_file.txt', 'w') as file:
    json.dump(my_dict, file)

with open('/Users/yuxi/Code/code-exercise/python基础/my_file.txt', 'r') as file:
    json_object = file.read()
    python_object = json.loads(json_object)
    print(type(python_object), python_object)

with open('/Users/yuxi/Code/code-exercise/python基础/my_file.txt', 'r') as file:
    python_object = json.load(file)
    print(type(python_object), python_object)
