# -*- coding:utf-8 -*-
from django.urls import path, re_path
from . import views

app_name = 'books'

urlpatterns = [
    re_path(r'^$', views.show_books),
    re_path(r'(\d+)', views.book_detail)
]
