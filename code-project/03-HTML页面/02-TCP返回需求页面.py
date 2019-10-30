# -*- coding:utf-8 -*-

"""
Name: 02-TCP返回需求页面.py
Author: fengdi
Datetime: 11:02 2019-07-08
Description:

"""
import re
import socket

HOST = ''
PORT = 12580
ADDR = (HOST, PORT)


# 请求处理函数
def handle_req(tmp_socket):
    """
    params：tmp_socket （通信使用的套接字）
    return: 服务器响应（需求页面）
    """
    # 接收客户端请求并打印
    recv_data = tmp_socket.recv(1024)
    req = recv_data.decode('utf-8')
    print(req)

    print('*' * 50)

    # 从请求信息中提取请求文件名
    file_name = ""
    req_lines = req.splitlines()  # 将请求信息字符串分割为字符串列表的形式
    print(req_lines)

    result = re.match(r"[^/]+(/[^ ]*)", req_lines[0])

    if result:
        file_name = result.group(1)  # 提取正则分组内请求文件名
        if file_name == "/":
            file_name = "/index.html"

    # 组织服务器响应
    try:
        f = open("./html" + file_name, "rb")
    except:
        response_header = "HTTP/1.1 404 NOT FOUND\r\n"
        response_body = "<h3>file not found</h3>"
        response = response_header + "\r\n" + response_body
        tmp_socket.send(response.encode("utf-8"))
    else:
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "\r\n"  # 添加空行
        file_content = f.read()
        f.close()
        response_body = file_content
        response = response_header.encode("utf-8") + response_body
        tmp_socket.send(response)


    # 关闭套接字
    tmp_socket.close()


def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 地址复用问题

    # 绑定地址
    tcp_server_socket.bind(ADDR)

    # 被动监听
    tcp_server_socket.listen(128)

    print('waiting for requests......')

    # 服务器循环
    while True:
        # 接收客户端连接
        tmp_socket, addr = tcp_server_socket.accept()

        # 使用临时套接字处理客户端请求
        handle_req(tmp_socket)

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
