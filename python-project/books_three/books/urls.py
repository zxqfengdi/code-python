# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^login/$', views.login),  # 登录页面
    url(r'^login_check/$', views.login_check),  # 登录校验
    url(r'^login_ajax/$', views.login_ajax),  # ajax页面
    url(r'^login_ajax_check/$', views.login_ajax_check)  # ajax登录校验
]
