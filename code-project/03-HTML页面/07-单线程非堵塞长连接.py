# -*- coding:utf-8 -*-

"""
Name: 07-单线程非堵塞长连接.py
Author: fengdi
Datetime: 7:54 下午 2019/10/31
Description: 
"""
import re
import socket


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
        self.tmp_socket_list = list()  # 创建列表保存接受连接产生的临时套接字引用
        self.server_socket.setblocking(False)  # 设置监听套接字非堵塞

    # 服务器监听
    def server_forver(self):
        while True:
            # 监听套接字非堵塞：需要进行异常处理，避免调用accept方法客户端还没有到来
            try:
                tmp_socket, addr = self.server_socket.accept()
            except Exception as e:
                pass
            # 没有异常说明有客户端到来
            else:
                tmp_socket.setblocking(False)  # 设置临时套接字非堵塞
                self.tmp_socket_list.append(tmp_socket)  # 将到来的客户端的套接字引用添加到列表内

            # 临时套接字非堵塞：需要进行异常处理，避免调用recv方法还没有请求过来
            for client in self.tmp_socket_list:
                try:
                    recv_data = client.recv(1024)
                except Exception as e:
                    pass
                else:
                    req = recv_data.decode("utf-8")
                    # 如果req有数据说明客户端发送了请求,有数据且长度为0说明客户端断开连接
                    if req:
                        self.handle_req(req, client)
                    else:
                        # 关闭套接字
                        client.close()
                        self.tmp_socket_list.remove(client)


    # 处理客户端请求
    def handle_req(self, req, tmp_socket):
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
            response_body = "------file not found------"
            response_header = "HTTP/1.1 404 NOT FOUND\r\n"
            response_header += "Content-Length: %d\r\n" % len(response_body)
            response_header += "\r\n"
            response = response_header + response_body
            tmp_socket.send(response.encode("utf-8"))
        else:
            content = f.read()
            f.close()
            response_body = content
            response_header = "HTTP/1.1 200 OK\r\n"
            response_header += "Content-Length: %d\r\n" % len(response_body)
            response_header += "\r\n"
            response = response_header.encode("utf-8") + response_body
            tmp_socket.send(response)

        # 关闭临时套接字(不关闭即长连接)
        # tmp_socket.close()


def main():
    # 创建服务器实例对象
    server = Wsgiserver()
    # 启动服务器
    server.server_forver()


if __name__ == '__main__':
    main()