# -*- coding:utf-8 -*-

"""
Name: 网络客户端编程.py
Author: fengdi
Datetime: 8:18 2019/5/13 
Description: 主要介绍网络客户端编程，包括文件传输、电子邮件等

"""

import ftplib
from email.mime.text import MIMEText
import smtplib
import poplib
from email.parser import Parser

# FTP编程

# 定义ftp服务器地址

HOST = '192.168.174.136'
USERNAME = 'fengdi'
PASSWD = '199618'

ADDR = (HOST, USERNAME, PASSWD)

# 建立ftp对象
f = ftplib.FTP(*ADDR)

# 连接ftp服务器
f.login()

# ftp操作
f.dir()

# 关闭ftp连接
f.close()


# 发送电子邮件

# 构造邮件信息

msg = MIMEText('Hello.send by python...', 'plain', 'utf-8')

# smtp发送邮件

# 发件人邮箱用户名密码
from_addr = input('From:')
passwd = input('Password:')

# 发件人邮箱SMTP服务器地址
smtp_server = input('SMTP server:')

# 收件人邮箱
to_addr = input('To:')

server = smtplib.SMTP(smtp_server, 25)
server.starttls()
server.set_debuglevel(1)  # 打印和SMTP服务器交互的信息
server.login(from_addr, passwd)  # 发件人邮箱登陆验证
server.sendmail(from_addr, [to_addr], msg.as_string())  # 发送邮件
server.quit()

# pop3接收邮件：使用poplib模块下载邮件，用emil模块解析邮件

# 邮箱名、密码、pop服务器地址
email_add = input('Email:')
password = input('Password:')
pop3_server = input('POP3 server:')

# 连接到pop3服务器
server = poplib.POP3_SSL(pop3_server)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

# 身份认证
server.user(email_add)
server.pass_(password)

# stat()返回邮件数量和占用空间
print('Messages: %s. Size: %s' % server.stat())
# list()返回所有邮件编号
resp, mails, octets = server.list()
print(mails)

# 获取最新一封邮件，索引号从1开始
index = len(mails)
resp, lines, octets = server.retr(index)

# lines里面存儲邮件原始文本的每一行
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 解析邮件
msg = Parser().parsestr(msg_content)

# 关闭连接
server.quit()
