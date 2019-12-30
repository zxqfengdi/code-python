# -*- coding:utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),  # 首页
    url(r'^temp_var/$', views.temp_var, name='temp_var'),  # 模板变量
    url(r'^temp_tags/$', views.temp_tags, name='temp_tags'),  # 模板标签
    url(r'^temp_filter/$', views.temp_filter, name='temp_filter'),  # 过滤器
    url(r'^my_def_filter/$', views.my_def_filter, name='my_def_filter'),  # 自定义过滤器
    url(r'^temp_inherit/$', views.temp_inherit, name='temp_inherit'),  # 模板继承
    url(r'^html_escape/$', views.html_escape, name='html_escape'),  # HTML转义
    url(r'^login/$', views.login, name='login'),  # 登录页面
    url(r'^login_check/$', views.login_check, name='login_check'),  # 登录检查
    url(r'^change_pwd/$', views.change_pwd, name='change_pwd'),  # 显示修改密码页面
    url(r'^change_pwd_action/$', views.change_pwd_action, name='change_pwd_action'),  # 密码修改操作
    url(r'^verify_code/$', views.verify_code, name='verify_code'),  # 产生验证码
]
