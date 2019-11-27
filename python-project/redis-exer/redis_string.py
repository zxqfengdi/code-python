# -*- coding:utf-8 -*-
# redis模块string类型操作练习
from redis import *


if __name__ == '__main__':
    try:
        # 创建 StrictRedis对象连接Redis服务器
        sr = StrictRedis()

        # string:增加键值对（set方法）
        result = sr.set('name', 'fengdi')

        # 打印结果：成功返回True,否则返回False
        print(result)

        # string:获取键对应的值（get方法）
        result = sr.get('name')

        # 键存在返回值，否则返回None
        print(result)

        # string:修改（键存在则为修改，否则为添加）
        result = sr.set('name', 'yuxi')

        # 打印结果：成功返回True,否则返回False
        print(result)

        # string:删除（根据键删除键值对，删除成功返回影响的函数，否则返回0）
        result = sr.delete('name')
        print(result)

        # string:获取键（根据正则，成功返回列表，否则返回空列表）
        result = sr.keys('*')
        print(result)

    except Exception as e:
        print(e)

