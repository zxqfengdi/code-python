# -*- coding:utf-8 -*-

"""
Name: urls.py
Author: fengdi
Datetime: 7:04 下午 2019/11/16
Description: 
"""
from django.urls import path
from . import views

urlpatterns = [
    path(r'index/', views.index),
    path(r'center/', views.center),
]
