# -*- coding:utf-8 -*-

"""
Name: 03-TCP返回需求页面多进程版.py
Author: fengdi
Datetime: 17:53 2019-07-08
Description:

"""
import re
import socket
import multiprocessing

HOST = ''
PORT = 12580
ADDR = (HOST, PORT)


# 使用面向对象实现
class Wsgiserver(object):

    # 服务器初始化
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(ADDR)
        self.server_socket.listen(128)

    # 服务器监听
    def server_forver(self):
        while True:
            tmp_socket, addr = self.server_socket.accept()
            # 收到客户端连接就创建一个进程进行请求处理
            t1 = multiprocessing.Process(target=self.handle_req, args=(tmp_socket,))
            t1.start()
            # 关闭临时套接字
            tmp_socket.close()

    # 处理客户端请求
    def handle_req(self, tmp_socket):
        recv_data = tmp_socket.recv(1024)
        req = recv_data.decode("utf-8")

        req_lines = req.splitlines()

        # 提取请求文件名
        result = re.match(r'[^/]+(/[^ ]*)', req_lines[0])

        file_name = ""
        if result:
            file_name = result.group(1)
            if file_name == "/":
                file_name = "/index.html"

        # 组织服务器响应
        try:
            f = open("./html" + file_name, 'rb')
        except:
            response_header = "HTTP/1.1 404 NOT FOUND\r\n"
            response_header += "\r\n"
            response_body = "------file not found------"
            response = response_header + response_body
            tmp_socket.send(response.encode("utf-8"))
        else:
            content = f.read()
            f.close()
            response_header = "HTTP/1.1 200 OK\r\n"
            response_header += "\r\n"
            response_body = content
            response = response_header.encode("utf-8") + response_body
            tmp_socket.send(response)

        # 关闭临时套接字
        tmp_socket.close()


def main():
    # 创建服务器实例对象
    server = Wsgiserver()
    # 启动服务器
    server.server_forver()


if __name__ == '__main__':
    main()
