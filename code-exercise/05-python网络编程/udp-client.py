# -*- coding:utf-8 -*-

"""
Name: udp-client.py
Author: fengdi
Datetime: 17:39 2019/5/13 
Description:

"""

import socket

# 定义要连接的服务端地址
HOST = ""
PORT = 7890
ADDR = (HOST, PORT)


def main():

    # 定义客户端套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 通信循环：收发消息
    while True:
        # 客户端先发送消息
        send_data = input("请输入要发送的数据：")

        if not send_data:
            break

        client_socket.sendto(send_data.encode("gbk"), ADDR)

        recv_data, addr = client_socket.recvfrom(1024)

        # 打印服务器发过来的数据
        print(recv_data.decode("gbk"))

    # 关闭客户端套接字
    client_socket.close()


if __name__ == '__main__':
    main()
