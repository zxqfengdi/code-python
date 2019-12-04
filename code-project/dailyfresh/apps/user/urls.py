from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    # url(r'^register/$', views.register, name='register'),  # 显示注册页面及注册验证(判断请求方法)
    # url(r'^register_handle/$', views.register_handle, name='register_handle'),  # 注册验证
    url(r'^register/$', views.RegisterView.as_view(), name='register'),  # 显示注册页面及注册验证(类视图)
    url(r'^active/(?P<token>.*)$', views.ActiveView.as_view(), name='active'),  # 用户激活
    url(r'^login/$', views.LoginView.as_view(), name='login'),  # 登录及登录验证（类视图）
    url(r'^logout/$', views.LoginOutView.as_view(), name='logout'),  # 退出登录（清除session信息）
    # url(r'^$', login_required(views.UserInfoView.as_view()), name='user'),  # 用户中心个人信息页面(使用login_required装饰器)
    # url(r'^order/$', login_required(views.UserOrderView.as_view()), name='order'),  # 用户中心订单页面
    # url(r'^site/$', login_required(views.UserSiteView.as_view()), name='site'),  # 用户中心收货地址

    url(r'^$', views.UserInfoView.as_view(), name='user'),  # 用户中心个人信息页面(使用Mixin类)
    url(r'^order/$', views.UserOrderView.as_view(), name='order'),  # 用户中心订单页面
    url(r'^site/$', views.UserSiteView.as_view(), name='site'),  # 用户中心收货地址
]
