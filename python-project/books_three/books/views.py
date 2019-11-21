from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


def index(request):
    """首页"""
    return HttpResponse('我是首页！')


def login(request):
    """登录页面"""
    # 先判断用户是否登录
    if request.session.has_key('isLogin'):
        # 之前已登录，跳转到首页
        return redirect('/books/index/')
    else:
        # 用户未登录
        # 获取cookie是否携带应户名信息
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
        else:
            username = ''

        context = {
            'username': username
        }

        return render(request, 'books/login.html', context)


def login_check(request):
    """登录校验"""
    # 1. 获取输入的用户名密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    print(remember)

    # 2. 校验（实际开发用户名密码存储在数据库中）
    if username == 'yuxi' and password == '123':
        # 数据正确:跳转首页
        response = redirect('/books/index/')
        # 勾选记住用户名，则设置cookie及过期时间
        if remember == 'on':
            response.set_cookie('username', username, max_age=7*24*3600)

        # 记住用户登录状态（如果用户登录时session中isLogin为True则直接跳转登录页面）
        request.session['isLogin'] = True

        return response
    else:
        # 数据错误：回到登录页
        return redirect('/books/login/')


def login_ajax(request):
    """显示ajax页面"""
    return render(request, 'books/login_ajax.html')


def login_ajax_check(request):
    """ajax登录校验"""
    # 1. 获取输入的用户名密码
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 2. 校验（实际开发用户名密码存储在数据库中）
    if username == 'yuxi' and password == '123':
        # 数据正确:跳转首页(返回的json数据：{'res': 1})
        context = {
            'res': 1
        }
        return JsonResponse(context)
    else:
        # 数据错误：显示提示信息(返回的json数据：{'res': 1})
        context = {
            'res': 0
        }
        return JsonResponse(context)


def set_cookie(request):
    """设置cookie信息"""
    response = HttpResponse('设置cookie')
    # 设置一个cookie信息
    response.set_cookie('num', '1')

    return response


def get_cookie(request):
    """获取浏览器携带的cookie"""
    cookie = request.COOKIES

    return HttpResponse(str(cookie))


def set_session(request):
    """设置session信息"""
    request.session['username'] = 'yuxi'
    request.session['age'] = 18

    return HttpResponse('设置session')


def get_session(request):
    """获取session信息"""
    username = request.session['username']
    age = request.session['age']

    return HttpResponse(username + ':' + str(age))
