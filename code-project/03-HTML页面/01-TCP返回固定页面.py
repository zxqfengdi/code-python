# -*- coding:utf-8 -*-

"""
Name: 01-TCP返回固定页面.py
Author: fengdi
Datetime: 17:52 2019-07-08
Description:

"""
import socket

HOST = ""
PORT = 7890
ADDR = (HOST, PORT)


# 定义请求处理函数
def handler_req(tmp_socket):

    # 接收请求信息并打印
    recv_data = tmp_socket.recv(1024).decode("utf-8")
    print(recv_data)
    print("*" * 50)

    # 组织响应头部信息
    response_header = "HTTP/1.1 200 OK\r\n"
    response_header += "\r\n"  # 空行分割body

    # 组织响应内容
    response_body = "hello world"
    print(response_body)
    response = response_header + response_body

    # 发送响应内容
    tmp_socket.send(response.encode("utf-8"))

    # 关闭临时套接字
    tmp_socket.close()


def main():

    # 创建tcp服务端套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定地址
    server_socket.bind(ADDR)

    # 监听连接
    server_socket.listen(5)

    # 接受客户端连接及请求处理
    while True:
        tmp_socket, addr = server_socket.accept()
        handler_req(tmp_socket)

    # 关闭套接字
    server_socket.close()


if __name__ == '__main__':
    main()
