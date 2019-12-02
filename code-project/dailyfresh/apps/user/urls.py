from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^register/$', views.register, name='register'),  # 显示注册页面及注册验证(判断请求方法)
    # url(r'^register_handle/$', views.register_handle, name='register_handle'),  # 注册验证
    url(r'^register/$', views.RegisterView.as_view(), name='register'),  # 显示注册页面及注册验证(类视图)
    url(r'^active/(?P<token>.*)$', views.ActiveView.as_view(), name='active'),  # 用户激活
    url(r'login/$', views.LoginView.as_view(), name='login'),  # 登录
]
