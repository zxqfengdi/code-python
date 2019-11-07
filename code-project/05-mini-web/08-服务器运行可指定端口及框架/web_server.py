# -*- coding:utf-8 -*-

"""
Name: web_server.py
Author: fengdi
Datetime: 11:27 2019-07-16
Description:

"""

import socket
import re
import sys
import multiprocessing


# TCP服务器类
class Wsgiserver(object):

    def __init__(self, port, app, static_path):
        """
        创建tcp服务器对象，绑定地址，开启监听
        :param port: TCP服务器端口号
        """
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(('', port))
        self.server_socket.listen(128)
        self.application = app
        self.static_path = static_path

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
                    f = open(self.static_path + file_name, "rb")
                except FileNotFoundError:
                    response_body = "------file not found------"

                    response_header = "HTTP/1.1 404 not found\r\n"
                    response_header += "Content-Type: text/html; charset=utf-8\r\n"
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
                env["file_info"] = file_name

                response_body = self.application(env, self.set_response_header)

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
        self.headers = [('server', 'mini_web v1.0')]
        self.headers += headers


def main():
    """
    主函数，控制整体
    :return:
    """
    input_argv = sys.argv

    if len(input_argv) == 3:

        try:
            port = int(input_argv[1])
            frame_app_name = input_argv[2]
        except ValueError as e:
            print("端口输入错误")
            return
    else:
        print("请按照下面方式运行：python3 xxxx.py 7890 mini_frame:application")
        return

    # 使用字符串split()方法
    ret = re.match(r'([^:]+):(.*)', frame_app_name)

    if ret:
        frame_name = ret.group(1)
        app_name = ret.group(2)
    else:
        print("请按照下面方式运行：python3 xxxx.py 7890 mini_frame:application")
        return

    # 将框架目录添加到搜索路径中
    with open("./web_server.conf") as f:
        conf_info = eval(f.read())

    sys.path.append(conf_info['dynamic_path'])
    static_path = conf_info['static_path']

    # 导入框架模块，返回值标记此模块
    frame = __import__(frame_name)

    # 返回值标记框架模块内的application函数
    app = getattr(frame, app_name)

    print("server running on port %s" % port)
    myserver = Wsgiserver(port, app, static_path)
    myserver.server_forever()


if __name__ == '__main__':
    main()
