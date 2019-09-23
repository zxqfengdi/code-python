# -*- coding:utf-8 -*-

"""
Name: udp-server.py
Author: fengdi
Datetime: 17:39 2019/5/13 
Description:

"""
import socket

# 定义服务器IP及端口

HOST = ""  # 字符串留空或者localhost代表本地，也可自定义Ip
PORT = 7890
ADDR = (HOST, PORT)


def main():
    # 定义服务器套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定地址
    server_socket.bind(ADDR)

    # 通信循环：收发消息
    while True:
        print("waiting for messages......")

        # 接受客户端消息
        recv_data, addr = server_socket.recvfrom(1024)
        print("receive messages:%s from %s" % (recv_data.decode("gbk"), str(addr)))

        if recv_data.decode("gbk") == "exit":
            break

        # 发送消息到客户端
        send_data = "我是UDP服务器，已接收到你发来的消息！"
        server_socket.sendto(send_data.encode("gbk"), addr)

    # 关闭服务端套接字
    server_socket.close()


if __name__ == '__main__':
    main()



