from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from celery_tasks.tasks import send_register_active_email
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from itsdangerous import SignatureExpired
from user.models import User
import re


# /user/register/
def register(request):
    """显示注册页面及注册验证"""
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        # 接收数据
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')

        # 数据校验:all方法--->判断所有数据完整性
        if not all([username, password, email]):
            return render(request, 'register.html', {'errmsg': '数据不完整'})

        # 校验邮箱
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
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


class RegisterView(View):
    """注册"""
    def get(self, request):
        """显示注册页面"""
        return render(request, 'register.html')

    def post(self, request):
        """注册验证"""
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')

        # 数据校验:all方法--->判断所有数据完整性
        if not all([username, password, email]):
            return render(request, 'register.html', {'errmsg': '数据不完整'})

        # 校验邮箱
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
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

        # 发送激活邮件，激活链接：http://127.0.0.1/user/active/1 （包含用户id：但是不能直接写id需要加密）
        # 激活链接中需要包含用户的身份信息

        # 1. 加密用户身份信息，生成激活token(使用Django的SECRET_KEY)
        serializer = Serializer(settings.SECRET_KEY, 3600)  # 过期时间：1小时
        info = {'confirm': user.id}

        token = serializer.dumps(info)  # bytes数据
        token = token.decode()

        # 发送邮件(使用delay方法将发送邮件任务添加到任务队列：中间人)
        send_register_active_email.delay(email, username, token)

        # 返回应答：注册成功跳转到首页
        return redirect(reverse('goods:index'))


class ActiveView(View):
    """用户激活"""
    def get(self, request, token):
        """激活"""
        # 1. 解密，获取用户信息
        serializer = Serializer(settings.SECRET_KEY, 3600)
        try:
            info = serializer.loads(token)
            # 获取待激活用户的id
            user_id = info['confirm']

            # 查询数据库，获取对应用户，改变激活状态
            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()

            # 激活成功，跳转登录界面
            return redirect(reverse('user:login'))
        except SignatureExpired:
            return HttpResponse('激活链接已过期')


class LoginView(View):
    """登录"""
    def get(self, request):
        """显示登录页面"""
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
            checked = 'checked'
        else:
            username = ''
            checked = ''

        context = {
            'username': username,
            'checked': checked
        }

        return render(request, 'login.html', context)

    def post(self, request):
        """登录校验"""
        # 1. 接收数据
        username = request.POST.get('username')
        password = request.POST.get("pwd")

        # 2. 数据校验
        # 完整性校验
        if not all([username, password]):
            return render(request, 'login.html', {'errmsg': '输入信息不完整'})

        # 校验用户名密码（使用内置认证系统的authenticate函数）
        user = authenticate(username=username, password=password)
        if user is not None:
            # 判断激活状态
            if user.is_active:
                # 用户已激活
                # 记录用户登录状态（使用内置认证系统的login函数：login函数会将当前用户的id写入到session信息表示其登录状态）
                login(request, user)

                # 跳转到首页
                response = redirect(reverse('goods:index'))

                # 判断是否记住用户名
                remember = request.POST.get('remember')
                if remember == 'on':
                    response.set_cookie('username', username, max_age=7*24*3600)
                else:
                    response.delete_cookie('username')

                return response
            else:
                # 用户未激活
                return render(request, 'login.html', {"errmsg": '账户未激活'})
        else:
            return render(request, 'login.html', {"errmsg": '用户名或密码错误'})


class UserInfoView(View):
    """用户中心"""
    # @login_required
    def get(self, request):
        """显示用户中心页面"""
        context = {
            'page_now': 'user'
        }
        return render(request, 'user_center_info.html', context)


class UserOrderView(View):
    """用户中心"""
    # @login_required
    def get(self, request):
        """显示用户中心页面"""
        context = {
            'page_now': 'order'
        }
        return render(request, 'user_center_order.html', context)


class UserSiteView(View):
    """用户中心"""
    # @login_required
    def get(self, request):
        """显示用户中心页面"""
        context = {
            'page_now': 'site'
        }
        return render(request, 'user_center_site.html', context)