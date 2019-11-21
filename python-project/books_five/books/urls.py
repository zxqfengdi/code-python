# -*- coding:utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^temp_var/$', views.temp_var),
    url(r'^temp_tags/$', views.temp_tags),
]
