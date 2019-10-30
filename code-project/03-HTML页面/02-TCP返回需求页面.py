# -*- coding:utf-8 -*-

"""
Name: 02-TCP返回需求页面.py
Author: fengdi
Datetime: 11:02 2019-07-08
Description:

"""
import socket
import re

HOST = ""
PORT = 7890
ADDR = (HOST, PORT)


# 定义请求处理函数
def handler_req(tmp_socket):

    # 接收请求数据
    recv_data = tmp_socket.recv(1024).decode("utf-8")
    print(recv_data)

    # 从请求数据内提取请求文件名（使用正则）
    request_lines = recv_data.splitlines()
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])

    file_name = ""
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"

    # 根据请求文件名打开文件读取,返回文件内容给客户端
    try:
        f = open("./html" + file_name, "rb")
    except:
        response_header = "HTTP/1.1 404 NOT FOUND\r\n"
        response_header += "\r\n"
        response_body = "------file not found------"
        response = response_header + response_body
        tmp_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "\r\n"
        response_body = html_content
        response = response_header.encode("utf-8") + response_body
        tmp_socket.send(response)

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
