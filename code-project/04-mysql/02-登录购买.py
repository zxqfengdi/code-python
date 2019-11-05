# -*- coding:utf-8 -*-

"""
Name: 02-登录购买.py
Author: fengdi
Datetime: 17:46 2019-07-13
Description:

"""
import time
from pymysql import *


class JD(object):

    login_username = ''
    login_password = ''

    def __init__(self):
        self.conn = connect(host='localhost', port=3306, user='root', password='199618',
                            database='jing_dong', charset='utf8')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    @staticmethod
    def exit():
        exit()

    def execute_sql(self, sql, params):
        result = self.cursor.execute(sql, params)
        return result

    def login(self):
        # 输入用户名密码登录，登录不成功转至注册
        name = input("请输入用户名：")
        passwd = input("请输入密码：")
        params = [name, passwd]
        print("正在登录京东商城........")

        # 从数据库customers表中取出所有用户名密码对比用户输入
        sql = """SELECT * FROM customers WHERE name=%s and passwd=%s"""
        count = self.execute_sql(sql, params)
        if count:
            print("登陆成功，欢迎光临京东商城！！！")
            JD.login_username = name
            JD.login_password = passwd
        else:
            print("您未注册京东账户，请进行注册！")
            self.register()

    def register(self):
        # 用户账号注册
        name = input("请输入用户名：")
        passwd = input("请输入密码：")
        address = input("请输入订单地址：")
        telphone = input("请输入联系电话：")
        params = [name, address, telphone, passwd]

        print("正在注册京东账户........")

        # 将用户输入的信息插入customers数据表中
        sql = """INSERT INTO customers(name, address, tel, passwd) VALUES (%s, %s, %s, %s)"""
        self.execute_sql(sql, params)
        self.conn.commit()
        print("注册成功，请重新登录")

    def show_goods(self):
        print("商品信息如下......")
        sql = """SELECT id, name, price FROM goods"""
        self.cursor.execute(sql)
        for item in self.cursor.fetchall():
            print(item)

    def buy(self):
        product_id = int(input("请输入商品ID:"))
        product_quality = int(input("请输入购买商品数量:"))
        order_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # 获取当前顾客id
        customer_sql = """SELECT id FROM customers WHERE name=%s AND passwd=%s"""
        params = [JD.login_username, JD.login_password]
        self.execute_sql(customer_sql, params)
        customer_id = self.cursor.fetchone()

        # 将订单信息插入订单表
        orders_sql = """INSERT INTO orders(order_date_time, customer_id) VALUES (%s, %s)"""
        self.cursor.execute(orders_sql, [order_time, customer_id])

        # 获取订单ID
        sql = """SELECT id FROM orders WHERE customer_id=%s"""
        params = [customer_id]
        self.execute_sql(sql, params)
        order_id = self.cursor.fetchall()

        # 将订单详情插入订单详情表
        order_detail_sql = """INSERT INTO order_detail(order_id, good_id, quality) VALUES (%s, %s, %s)"""
        params = [order_id, product_id, product_quality]
        self.execute_sql(order_detail_sql, params)
        self.conn.commit()

        print("订单提交成功！！！")

    def show_shopping_cart(self):
        pass

    @staticmethod
    def print_menu():
        print("------------------------京东商城-------------------------")
        print("1:登录账号 2:注册账号 3:商品信息 4:商品购买 5:查看购物车 q:退出商城")
        return input("请输入功能选项：")

    def run(self):
        while True:
            num = self.print_menu()

            if num == "1":
                self.login()
            elif num == "2":
                self.register()
            elif num == "3":
                self.show_goods()
            elif num == "4":
                self.buy()
            elif num == "5":
                self.show_shopping_cart()
            elif num == "q":
                self.exit()
            else:
                print("输入错误，请重新输入：")


def main():
    jd = JD()
    jd.run()


if __name__ == '__main__':
    main()
