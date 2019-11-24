# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ip_test/$', views.ip_test, name='ip_test'),
    url(r'^show_upload/$', views.show_upload, name='show_upload'),
    url(r'^upload_handle/$', views.upload_handle, name='upload_handle'),
    url(r'^show_areas/$', views.show_areas, name='show_areas'),
]
