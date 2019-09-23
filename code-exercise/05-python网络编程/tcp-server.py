# -*- coding:utf-8 -*-

"""
Name: tcp-server.py
Author: fengdi
Datetime: 16:04 2019/5/13 
Description: tcp服务器代码

"""

import socket

# 定义服务器地址：主机名/ip、端口号
Host = ''
PORT = 7890
ADDR = (Host, PORT)


def main():

    # 定义TCP套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定地址
    server_socket.bind(ADDR)

    # 开始监听（变为被动）
    server_socket.listen(128)

    # 通信循环：用来循环接受客户端连接
    while True:

        # 接受客户端连接
        tmp_socket, addr= server_socket.accept()  # 返回一个临时套接字（用于客户端通信）及客户端的地址
        print("connect from :", addr)

        # 通信循环：使用临时套接字收发数据
        while True:
            recv_data = tmp_socket.recv(1024)

            if not recv_data:
                break

            print(recv_data.decode("gbk"))

            send_data = "我是一个TCP服务器！！"
            tmp_socket.send(send_data.encode("gbk"))

        tmp_socket.close()  # 关闭临时套接字

    server_socket.close()  # 关闭监听套接字


if __name__ == '__main__':
    main()