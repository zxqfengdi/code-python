# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_books),
    url(r'(\d+)', views.book_detail)  # 使用分组（分组匹配的值传递到处理函数内部）
]
