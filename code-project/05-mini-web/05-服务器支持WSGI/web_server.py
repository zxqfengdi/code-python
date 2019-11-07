# -*- coding:utf-8 -*-

"""
Name: web_server.py
Author: fengdi
Datetime: 19:10 2019-07-15
Description:

"""

import socket
import re
import time
import mini_frame
import multiprocessing

# 定义TCP服务器地址
HOST = ""
PORT = 7890
server_addr = (HOST, PORT)


# TCP服务器类
class Wsgiserver(object):

    def __init__(self, addr):
        """
        创建tcp服务器对象，绑定地址，开启监听
        :param addr: TCP服务器地址
        """
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(addr)
        self.server_socket.listen(128)

    def server_forever(self):
        """
        循环处理客户端连接
        :return:
        """
        while True:
            tmp_socket, addr = self.server_socket.accept()
            t1 = multiprocessing.Process(target=self.handler_req, args=(tmp_socket, ))
            t1.start()
            tmp_socket.close()
        self.server_socket.close()

    # 定义请求处理函数
    def handler_req(self, client_socket):
        """
        对客户端请求进行处理，返回需求数据
        :param client_socket: 临时套接字，与一个客户端通信
        :return: 返回请求资源，未找到返回404
        """

        # 长连接方式：接收请求数据
        while True:
            try:
                recv_data = client_socket.recv(1024).decode("utf-8")
                print(recv_data)
            except Exception as ret:
                print(">" * 50, ret)
                client_socket.close()
                return

            # 判断浏览器是否关闭
            if not recv_data:
                client_socket.close()
                return

            # 从请求数据内提取请求文件名
            request_lines = recv_data.splitlines()
            ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])

            file_name = ""
            if ret:
                file_name = ret.group(1)
                if file_name == "/":
                    file_name = "/index.html"

            if not file_name.endswith('.py'):
                # 根据请求文件名打开文件读取,返回文件内容给客户端
                try:
                    f = open("./html" + file_name, "rb")
                except FileNotFoundError:
                    response_body = "------file not found------"

                    response_header = "HTTP/1.1 404 not found\r\n"
                    response_header += "Content-Length: %d\r\n" % (len(response_body))
                    response_header += "\r\n"

                    response = response_header + response_body
                    client_socket.send(response.encode("utf-8"))
                else:
                    html_content = f.read()
                    f.close()
                    response_body = html_content

                    response_header = "HTTP/1.1 200 OK\r\n"
                    response_header += "Content-Length: %d\r\n" % (len(response_body))
                    response_header += "\r\n"

                    response = response_header.encode("utf-8") + response_body
                    client_socket.send(response)
            else:
                env = dict()
                response_body = mini_frame.application(env, self.set_response_header)

                response_header = "HTTP/1.1 %s\r\n" % self.status
                response_header += "Content-Length: %d\r\n" % (len(response_body.encode("utf-8")))

                for temp in self.headers:
                    response_header += "%s:%s\r\n" % (temp[0], temp[1])

                response_header += "\r\n"

                response = response_header + response_body
                client_socket.send(response.encode("utf-8"))

        client_socket.close()

    def set_response_header(self, status, headers):
        self.status = status
        self.headers = headers


def main():
    """
    主函数，控制整体
    :return:
    """
    myserver = Wsgiserver(server_addr)
    print("server running on port %s" % PORT)
    myserver.server_forever()


if __name__ == '__main__':
    main()
