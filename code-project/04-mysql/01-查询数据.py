# -*- coding:utf-8 -*-

"""
Name: 01-查询数据.py
Author: fengdi
Datetime: 11:38 2019-07-13
Description:

"""
from pymysql import *


class JD(object):

    def __init__(self):
        self.connect = connect(host='localhost', port=3306, user='root',
                               password='199618', database='jing_dong', charset='utf8')
        self.cursor = self.connect.cursor()

    def __del__(self):
        self.cursor.close()
        self.connect.close()

    def excute_sql(self, sql):
        self.cursor.execute(sql)
        for item in self.cursor.fetchall():
            print(item)

    def search_all(self):
        """
        查询所有商品信息
        :return: 所有商品信息
        """
        sql = "SELECT * FROM goods"
        self.excute_sql(sql)

    def search_cates(self):
        """
        查询商品种类
        :return: 商品种类信息
        """
        sql = "SELECT name FROM goods_cates"
        self.excute_sql(sql)

    def search_brands(self):
        """
        查询商品品牌
        :return: 商品品牌信息
        """
        sql = "SELECT name FROM goods_brands"
        self.excute_sql(sql)

    @staticmethod
    def print_menu():
        print("-----------------京东商城-----------------")
        print("1：查询所有商品 2：查询商品种类 3：查询商品品牌 q：退出查询")
        flag = input("请输入功能序号：")
        return flag

    def run(self):

        while True:
            flag = self.print_menu()

            if flag == "1":
                self.search_all()
            elif flag == "2":
                self.search_cates()
            elif flag == "3":
                self.search_brands()
            elif flag == "q":
                break
            else:
                print("输入有误，请重新输入：")


def main():

    # 创建京东商城对象
    jd = JD()

    # 调用对象run方法
    jd.run()


if __name__ == '__main__':
    main()
