# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^login/$', views.login),  # 登录页面
    url(r'^login_check/$', views.login_check),  # 登录校验
    url(r'^login_ajax/$', views.login_ajax),  # ajax页面
    url(r'^login_ajax_check/$', views.login_ajax_check),  # ajax登录校验
    url(r'^set_cookie/$', views.set_cookie),  # 设置cookie
    url(r'^get_cookie/$', views.get_cookie),  # 获取cookie
    url(r'^set_session/$', views.set_session),  # 设置session
    url(r'^get_session/$', views.get_session),  # 获取session
]
