# -*- coding:utf-8 -*-

"""
Name: 数据库编程.py
Author: fengdi
Datetime: 9:58 2019/5/14 
Description: 主要介绍python中数据库编程的相关知识

"""

import sqlite3
import pymysql


# python连接mysql

# 创建connection对象
conn = pymysql.connect(host="localhost", port=3306, database="python_test",
                       user="yuxi", password="199618", charset="utf8")

if conn:
    print("连接数据库成功！")

# 创建cursor对象
cursor = conn.cursor()

# 定义sql执行语句
select_sql = """SELECT * FROM students;"""

# 使用游标对象执行sql语句，返回受影响的行数
count = cursor.execute(select_sql)
print("查出%d条数据" % count)

for info in range(count):
    print(cursor.fetchone())


# 关闭游标对象
cursor.close()

# 关闭connection对象
conn.close()

# python连接sqlite3
# 创建connection对象连接数据库，文件不存在则会在当前目录新建
conn = sqlite3.connect('sqlite-test.db')
# 创建游标对象
cursor = conn.cursor()
# 执行SQL语句，创建user表
cursor.execute('CREATE TABLE user (id varchar(20) primary key, name varchar(20))')
# 执行SQL语句，插入一条记录
cursor.execute('INSERT INTO user (id, name) values (\'1\', \'fengdi\')')
data = cursor.rowcount
print('插入记录：%d条' % data)
# 关闭游标
cursor.close()
# 事务提交：对数据库、数据表进行更改后需要提交
conn.commit()
# 关闭数据库连接
conn.close()