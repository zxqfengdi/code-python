# -*- coding:utf-8 -*-

"""
Name: 01-TCP返回固定页面.py
Author: fengdi
Datetime: 17:52 2019-07-08
Description:

"""
import socket

HOST = ''
PORT = 12580
ADDR = (HOST, PORT)


# 请求处理函数
def handle_req(tmp_socket):
    """
    params：tmp_socket （通信使用的套接字）
    return: 服务器响应（固定页面）
    """
    # 接收客户端请求并打印
    recv_data = tmp_socket.recv(1024)
    req = recv_data.decode('utf-8')
    print(req)

    print('*' * 50)

    # 组织服务器响应(响应头部和响应主体以空行分割)
    response_header = 'HTTP/1.1 200 OK\r\n'

    response_boby = '<h1>hello world</h1><p>我是服务器返回的页面内容</p>'

    response = response_header + '\r\n' + response_boby

    tmp_socket.send(response.encode('utf-8'))

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
