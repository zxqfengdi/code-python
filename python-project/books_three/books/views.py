from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


def index(request):
    """首页"""
    return HttpResponse('我是首页！')


def login(request):
    """登录页面"""
    return render(request, 'books/login.html', {})


def login_check(request):
    """登录校验"""
    # 1. 获取输入的用户名密码
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 2. 校验（实际开发用户名密码存储在数据库中）
    if username == 'smart' and password == '123':
        # 数据正确:跳转首页
        return redirect('/books/index/')
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
