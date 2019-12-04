from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from celery_tasks.tasks import send_register_active_email
from django.contrib.auth import authenticate, login, logout
from django_redis import get_redis_connection
from utils.mixin import LoginRequiredMixin
from itsdangerous import SignatureExpired
from user.models import User, Address
from goods.models import GoodsSKU
import re


# /user/register/
# def register(request):
#     """显示注册页面及注册验证"""
#     if request.method == 'GET':
#         return render(request, 'register.html')
#
#     if request.method == 'POST':
#         # 接收数据
#         username = request.POST.get('user_name')
#         password = request.POST.get('pwd')
#         email = request.POST.get('email')
#         allow = request.POST.get('allow')
#
#         # 数据校验:all方法--->判断所有数据完整性
#         if not all([username, password, email]):
#             return render(request, 'register.html', {'errmsg': '数据不完整'})
#
#         # 校验邮箱
#         if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
#             return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})
#
#         if allow != 'on':
#             return render(request, 'register.html', {'errmsg': '请同意协议'})
#
#         # 校验用户名是否已经注册
#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             # 抛出异常说明用户名可用
#             user = None
#
#         if user:
#             # 用户名已存在
#             return render(request, 'register.html', {'errmsg': '用户名重复'})
#
#         # 业务处理：用户注册
#         user = User.objects.create_user(username, email, password)
#         user.is_active = 0  # 默认账户未激活
#         user.save()
#         # 返回应答：注册成功跳转到首页
#         return redirect(reverse('goods:index'))


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

                # 获取登录后要跳转的地址(默认值)
                next_url = request.GET.get('next', reverse('goods:index'))

                # 跳转到首页
                response = redirect(next_url)

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


class LoginOutView(View):
    """退出登录"""
    def get(self, request):
        # 内置认证系统的logout函数退出登录：清除相关数据（login函数写到session信息里面的登录状态信息）
        logout(request)
        return redirect(reverse('goods:index'))


class UserInfoView(LoginRequiredMixin, View):
    """用户中心"""
    def get(self, request):
        """显示用户中心页面"""
        # 获取用户个人信息
        user = request.user
        # try:
        #     address = Address.objects.get(user=user, is_default=True)
        # except Address.DoesNotExist:
        #     # 如果没有默认收货地址相关信息应跳转到地址页面进行添加
        #     address = None
        address = Address.objects.get_default_address_obj(user)

        # 获取用户历史信息
        con = get_redis_connection('default')
        history_key = 'history_%d' % user.id
        # 获取用户最新浏览的5个商品id
        sku_ids = con.lrange(history_key, 0, 4)

        # 根据sku_id查询历史浏览商品信息
        goods_info = []
        for sku_id in sku_ids:
            goods = GoodsSKU.objects.get(id=sku_id)
            goods_info.append(goods)

        context = {
            'page_now': 'user',
            'user': user,
            'address': address,
            'goods_info': goods_info
        }
        return render(request, 'user_center_info.html', context)


class UserOrderView(LoginRequiredMixin, View):
    """用户中心"""
    def get(self, request):
        """显示用户中心页面"""
        # 获取用户订单信息
        context = {
            'page_now': 'order'
        }
        return render(request, 'user_center_order.html', context)


class UserSiteView(LoginRequiredMixin, View):
    """用户中心"""
    def get(self, request):
        """显示用户中心页面"""
        # 获取用户默认收货地址
        user = request.user  # 代表登录的用户
        # try:
        #     address = Address.objects.get(user=user, is_default=True)
        # except Address.DoesNotExist:
        #     address = None
        # 调用自定义模型管理器对象的自定义方法
        address = Address.objects.get_default_address_obj(user)

        context = {
            'page_now': 'site',
            'address': address
        }
        return render(request, 'user_center_site.html', context)

    def post(self, request):
        """提交收货信息"""
        # 接收数据
        receiver = request.POST.get("receiver")
        addr = request.POST.get("addr")
        zip_code = request.POST.get("zipcode")
        phone = request.POST.get("phone")

        # 校验数据
        # 完整性校验
        if not all([receiver, addr, phone]):
            return render(request, 'user_center_site.html', {'errmsg': '数据不完整'})

        # 校验手机号
        if not re.match(r'^1[3|4|5|6|7|8][0-9]{9}$', phone):
            return render(request, 'user_center_site.html', {'errmsg': '手机号格式错误'})

        # 业务处理：添加地址（如果用户存在默认收货地址，则添加的地址不作为默认收货地址）
        user = request.user  # 代表登录的用户
        # try:
        #     address = Address.objects.get(user=user, is_default=True)
        # except Address.DoesNotExist:
        #     address = None
        address = Address.objects.get_default_address_obj(user)

        if address:
            # 说明已存在默认收货地址
            is_default = False
        else:
            # 说明不存在收货地址
            is_default = True

        # 添加地址
        Address.objects.create(user=user,
                               receiver=receiver,
                               addr=addr,
                               zip_code=zip_code,
                               phone=phone,
                               is_default=is_default)

        # 返回响应
        return redirect(reverse('user:site'))
