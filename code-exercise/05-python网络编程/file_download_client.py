# -*- coding:utf-8 -*-

"""
Name: file_download_client.py
Author: fengdi
Datetime: 10:28 2019-07-04
Description: 使用TCP套接字建立文件下载器客户端

"""

import socket


def main():

    # 创建套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 获取服务器的Ip和port
    dest_ip = input("请输入服务器ip:")
    dest_port = input("请输入服务器port:")

    # 连接服务器
    client_socket.connect((dest_ip, int(dest_port)))

    # 获取下载文件名字
    file_name = input("请输入下载文件名称：")

    # 发送文件名字到服务器
    client_socket.send(file_name.encode("utf-8"))

    # 接受文件数据
    recv_data = client_socket.recv(1024)

    # 保存数据到文件
    if recv_data:
        with open('下载' + file_name, 'wb') as f:
            f.write(recv_data)

    # 关闭套接字
    client_socket.close()


if __name__ == '__main__':
    main()
