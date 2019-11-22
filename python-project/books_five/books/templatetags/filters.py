# -*- coding:utf-8 -*-
from django.template import Library

# 创建Library的对象
register = Library()


# 自定义过滤器
@register.filter
def mod(num):
    """判断是否为偶数"""
    return num%2 == 0

