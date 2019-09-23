# -*- coding:utf-8 -*-

"""
Name: 04-TCP返回需求页面多线程版.py
Author: fengdi
Datetime: 17:54 2019-07-08
Description:

"""
import socket
import re
import threading

HOST = ""
PORT = 7890
ADDR = (HOST, PORT)


class Wsgiserver(object):

    def __init__(self, addr):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(addr)
        self.server_socket.listen(128)

    def server_forever(self):
        while True:
            tmp_socket, addr = self.server_socket.accept()
            t1 = threading.Thread(target=self.handler_req, args=(tmp_socket, ))
            t1.start()

        self.server_socket.close()

    # 定义请求处理函数
    def handler_req(self, tmp_socket):

        # 接收请求数据
        recv_data = tmp_socket.recv(1024).decode("utf-8")
        print(recv_data)

        # 从请求数据内提取请求文件名
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

        tmp_socket.close()


def main():
    myserver = Wsgiserver(ADDR)
    print("server running on port %s" % PORT)
    myserver.server_forever()


if __name__ == '__main__':
    main()
