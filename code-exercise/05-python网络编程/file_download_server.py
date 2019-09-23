# -*- coding:utf-8 -*-

"""
Name: file_download_server.py.py
Author: fengdi
Datetime: 10:26 2019-07-04
Description: 使用TCP套接字建立文件下载器服务器端

"""

import socket

HOST = "192.168.31.199"
PORT = 7890
ADDR = (HOST, PORT)


def send_content(tmp_socket, addr):

    print("客户端%s已连接....." % str(addr))

    # 接受下载文件名称
    file_name = tmp_socket.recv(1024)

    content = None

    try:
        with open(file_name, 'rb') as f:
            content = f.read()
    except Exception as e:
        print("没有找到要下载的文件！")

    # 判断是否读取到文件内容
    if content:
        tmp_socket.send(content)


def main():

    # 创建套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定地址
    server_socket.bind(ADDR)

    # 监听请求
    server_socket.listen(5)

    # 循环接收连接
    while True:

        # 接受客户端连接
        tmp_socket, addr = server_socket.accept()

        # 调用函数发送文件内容给客户端
        send_content(tmp_socket, addr)

        # 关闭套接字
        tmp_socket.close()

    server_socket.close()


if __name__ == '__main__':
    main()

