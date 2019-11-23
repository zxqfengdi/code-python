# -*- coding:utf-8 -*-
from django.http import HttpResponse


# 中间件类
class BlockIpMiddleWare(object):
    EXCLUDE_IPS = ['192.168.31.157']

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        """中间件函数：视图函数调用前调用"""
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in BlockIpMiddleWare.EXCLUDE_IPS:
            return HttpResponse('<h1>Forbidden</h1>')


