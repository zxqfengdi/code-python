from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),  # 显示注册页面
    url(r'^register_handle/$', views.register_handle, name='register_handle'),  # 注册验证
]
