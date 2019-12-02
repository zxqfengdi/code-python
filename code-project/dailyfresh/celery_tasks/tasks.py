# -*- coding:utf-8 -*-
from django.conf import settings
from django.core.mail import send_mail
from celery import Celery

# 创建Celery类实例对象
app = Celery('celery_tasks.tasks', broker='redis://192.168.31.199:6379/7')


# 定义任务函数（使用装饰器将任务注册到broker队列中）
@app.task
def send_register_active_email(to_email, username, token):
    """发送激活邮件"""
    # 组织邮件信息
    subject = '天天生鲜欢迎信息'
    html_message = '<h1>%s, 欢迎您成为天天生鲜注册会员！</h1>请点击以下链接激活账户：<a href="http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a>' % (username, token, token)
    from_email = settings.EMAIL_FROM
    recipient_list = [to_email]

    send_mail(subject=subject, message='', from_email=from_email, recipient_list=recipient_list, html_message=html_message)
