from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from user.models import User
import re


# /user/register/
def register(request):
    """显示注册页面"""
    return render(request, 'register.html')


# /user/register_handle/
def register_handle(request):
    """注册处理"""
    # 接收数据
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')
    allow = request.POST.get('allow')

    # 数据校验:all方法--->判断所有数据完整性
    if not all([username, password, email]):
        return render(request, 'register.html', {'errmsg': '数据不完整'})

    # 校验邮箱
    if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})

    if allow != 'on':
        return render(request, 'register.html', {'errmsg': '请同意协议'})

    # 校验用户名是否已经注册
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        # 抛出异常说明用户名可用
        user = None

    if user:
        # 用户名已存在
        return render(request, 'register.html', {'errmsg': '用户名重复'})

    # 业务处理：用户注册
    user = User.objects.create_user(username, email, password)
    user.is_active = 0  # 默认账户未激活
    user.save()

    # 返回应答：注册成功跳转到首页
    return redirect(reverse('goods:index'))
