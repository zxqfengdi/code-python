# -*- coding:utf-8 -*-

"""
Name: tcp-client.py
Author: fengdi
Datetime: 16:22 2019/5/13 
Description:tcp客户端代码

"""

import socket

# 定义要连接的服务器端地址
Host = ""
PORT = 7890
ADDR = (Host, PORT)


def main():

    # 定义tcp客户端套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接tcp服务器
    client_socket.connect(ADDR)

    # 通信循环：收发数据

    while True:

        send_data = input("请输入要发送的数据：")

        # 发送数据给服务器
        client_socket.send(send_data.encode("gbk"))

        # 从服务器接收数据并打印
        recv_data = client_socket.recv(1024)

        if not recv_data:
            break
        print(recv_data.decode("gbk"))

    client_socket.close()


if __name__ == '__main__':
    main()
