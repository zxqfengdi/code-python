# -*- coding:utf-8 -*-

"""
Name: 08-epoll版实现并发服务器.py
Author: fengdi
Datetime: 9:10 上午 2019/11/1
Description: 
"""
import socket
import re
import select

HOST = ""
PORT = 12580
ADDR = (HOST, PORT)


class WSGIServer(object):
    """定义一个WSGI服务器的类"""

    def __init__(self):

        # 1. 创建套接字
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2. 绑定本地信息
        self.server_socket.bind(ADDR)

        # 3. 变为监听套接字
        self.server_socket.listen(128)

        # 创建epoll对象(轮询对象)
        self.epoll = select.epoll()

        # 将tcp服务器套接字加入到epoll中进行监听
        self.epoll.register(self.server_socket.fileno(), select.EPOLLIN|select.EPOLLET)

        # 创建添加的fd对应的套接字
        self.fd_socket = dict()

    def run_forever(self):
        """运行服务器"""

        # 等待对方链接
        while True:
            # epoll 进行fd扫描的地方 -- 未指定超时时间则为阻塞等待（默认堵塞直到套接字对应的文件描述符有写入事件）
            epoll_list = self.epoll.poll()

            # 对事件进行判断
            for fd, event in epoll_list:
                # 如果是服务器套接字可以收数据，那么意味着可以进行accept
                if fd == self.server_socket.fileno():
                    new_socket, new_addr = self.server_socket.accept()

                    # 向 epoll中注册临时套接字的文件描述符
                    self.epoll.register(new_socket.fileno(), select.EPOLLIN | select.EPOLLET)

                    # 记录这个文件描述符和对应的套接字到字典中
                    self.fd_socket[new_socket.fileno()] = new_socket
                # 接收到数据（客户端发送请求）
                elif event == select.EPOLLIN:
                    request = self.fd_socket[fd].recv(1024).decode("utf-8")
                    if request:
                        self.deal_with_request(request, self.fd_socket[fd])
                    else:
                        # 在epoll中注销客户端的信息
                        self.epoll.unregister(fd)
                        # 关闭客户端的文件句柄
                        self.fd_socket[fd].close()
                        # 在字典中删除与已关闭客户端相关的信息
                        del self.fd_socket[fd]

    def deal_with_request(self, request, client_socket):
        """为这个浏览器服务器"""

        if not request:
            return

        request_lines = request.splitlines()
        for i, line in enumerate(request_lines):
            print(i, line)

        # 提取请求的文件
        ret = re.match(r"([^/]*)([^ ]+)", request_lines[0])
        file_name = ""

        if ret:
            print("正则提取数据:", ret.group(1))
            print("正则提取数据:", ret.group(2))
            file_name = ret.group(2)
            if file_name == "/":
                file_name = "/index.html"


        # 读取文件数据
        try:
            f = open('./html' + file_name, "rb")
        except:
            response_body = "file not found, 请输入正确的url"

            response_header = "HTTP/1.1 404 not found\r\n"
            response_header += "Content-Type: text/html; charset=utf-8\r\n"
            response_header += "Content-Length: %d\r\n" % len(response_body)
            response_header += "\r\n"

            # 将header返回给浏览器
            client_socket.send(response_header.encode('utf-8'))

            # 将body返回给浏览器
            client_socket.send(response_body.encode("utf-8"))
        else:
            content = f.read()
            f.close()

            response_body = content

            response_header = "HTTP/1.1 200 OK\r\n"
            response_header += "Content-Length: %d\r\n" % len(response_body)
            response_header += "\r\n"

            # 将数据返回给浏览器
            client_socket.send(response_header.encode("utf-8")+response_body)


def main():
    """控制web服务器整体"""
    http_server = WSGIServer()
    http_server.run_forever()


if __name__ == "__main__":
    main()