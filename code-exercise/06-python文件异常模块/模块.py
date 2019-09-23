# -*- coding:utf-8 -*-

"""
Name: 模块.py
Author: fengdi
Datetime: 20:14 2019/5/9 
Description: 主要介绍常用的python内置模块的相关内容

"""

# 模块：一个python文件就是一个模块。模块内通常用：if __name__ == "__main__"定义用户接口
# 包：可使用包来组织模块，避免模块名冲突。包里面一般包含一个__init__文件（表示当前目录为包。）一个__pycache__目录，缓存每个模块编译后的文件（pyc文件）。
# 模块导入搜索路径：先搜索当前目录，再搜索所有已安装和第三方模块。可使用sys.path获取

import sys
import os
import shutil
import glob
import time
from _datetime import datetime
import collections
import hashlib
from urllib import request

print(sys.path)

# 常用内置模块：os(操作系用和文件目录操作)、time(时间处理模块)、datetime模块等。
# os模块:文件处理

print(dir(os))
print(os.name, os.uname())   # 查看系统信息
print(os.environ)       # 查看环境变量  os.environ(key)获得某个键的值
os.mkdir('path')        # 创建目录
os.rmdir('path')        # 删除目录，尽量使用绝对路径
os.makedirs('path')       # 递归创建目录
os.removedirs('path')   # 递归删除目录
os.listdir('path')      # 列出目录下文件
os.remove('test.py')    # 删除文件
os.rename('file1', 'file2')     # 重命名文件或目录
os.chmod('file',mode=1)                # 修改文件权限
os.chown('file',gid=65498, uid=65198)                # 修改文件所有者所属组
print(os.stat('file'))          # 查看文件的附加信息
os.symlink('file', 'soft_link_test')   # 为文件创建软链接
print(os.getcwd())          # 查询当前工作目录
os.chdir('path')            # 修改工作目录

# shutil模块：复制、移动、递归删除、修改工作目录

print(dir(shutil))
shutil.copy('path', 'path')             # 复制文件
shutil.copyfile('path', 'path')   # 复制文件
shutil.move('path', 'path')         # 移动文件

# os.path模块：处理路径字符串

print(os.path.basename('path'))   # 查询路径中包含的文件名
print(os.path.dirname('path'))    # 查询路径中包含的目录
print(os.path.abspath('path'))    # 查询文件或目录的绝对路径
os.path.join('path', 'file')    # 使用目录和文件构造一个路径
os.path.split('path')           # 拆分路径，后一部分为最后级别的目录名或文件名
os.path.splitext('path')        # 获得文件名及扩展名
os.path.exists('path')          # 查询文件或目录是否存在
os.path.getatime('path')        # 获取文件最后读取时间
os.path.getctime('path')        # 获取文件最后修改时间
os.path.getsize('path')         # 查询文件大小
os.path.isfile('path')          # 路径对应的是否为文件
os.path.isdir('path')            # 路径对应的是否为目录

# glob模块：通配符，列出所有符合表达式的文件
print(glob.glob("pattern"))
print(glob.glob('*.py'))   # 列出所有以.py结尾的文件

# time模块：时间处理

print(time.time())      # 返回以秒为单位的浮点数时间（Unix时间戳，1971.1.1 00：00：00 UTC）
print(time.clock())     # 返回处理器时间
time.sleep(3)           # 休眠N秒
print(time.ctime())     # 将以秒为单位的时间（time.time()）转换为当地时间的字符串
print(time.asctime())   # 将时间元组转换为当地时间的时间元组
print(time.localtime()) # 将以秒为单位的时间转换为当地时间的时间元组
print(time.gmtime())    # 将以秒为单位的时间转换为UTC时间的时间元组
print(time.mktime())    # 将时间元组转换为挂钟时间

# datetime模块：对time模块进行封装，包含多个日期时间处理模块(from datetime import datetime)

print(datetime.now())       # 返回一个datetime对象，表示当地时间
print(datetime.utcnow())    # 返回一个datetime对象，表示UTC时间
object_datetime = datetime.now()
object_datetime.timestamp() # 将一个datetime对象转换为unix时间戳
datetime.fromtimestamp() # 将unix时间戳转换为datetime对象
datetime.strftime(object_datetime)   # 将datetime对象格式化为字符串
datetime.strptime()     # 将时间字符串转换为datetime对象

# collections:python内置的集合模块，提供很多有用的集合类。
# namedtuple:命名元组，为一个函数，可用来创建一个自定义的tuple对象。其可规定元素的个数，并可使用属性（不是索引）来访问某个元素
# 语法：namedtuple('name', [元素])

Circle = collections.namedtuple('Circle', ['x', 'y', 'z'])
print(isinstance(Circle, tuple))
circle = Circle(5, 6, 7)
print(circle.x, circle.y, circle.z)

# deque:列表list为先行存储，数据量较大时，插入删除效率较低。deque是可实现高效插入和删除的双向列表，适合用于队列和栈。
# deque不仅实现了list的append和pop，还支持appendleft()和popleft().

deque_list = collections.deque([1, 2, 3])
print(type(deque_list))
deque_list.appendleft(5)
deque_list.append(6)
print(deque_list)

# hashlib模块：提供常用的摘要算法，如MD5,SHA1等。摘要算法：通过一个函数，将任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）

md5 = hashlib.md5()
md5.update("how to use md5 in python hashlib?".encode('utf-8'))
print(md5.hexdigest())


# urllib模块：提供了一系列操作URL的功能

with request.urlopen("http://fengdi.org/2017/08/10/Hexo.html") as f:
    data = f.read()
    print("status:", f.status, f.reason)
    for k, v in f.getheaders():
        print("%s: %s" % (k, v))
print('Data:', data.decode('utf-8'))

# 常用第三方模块：requests Pillow chardet psutil模块
