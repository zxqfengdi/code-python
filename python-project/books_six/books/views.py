from django.shortcuts import render
from django.http import HttpResponse
from books.models import BookInfo

# 禁止访问的IP列表
EXCLUDE_IPS = ['192.168.31.157']


# 禁止访问装饰器
def blocked_ips(view_func):
    def inner(request, *args, **kwargs):
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in EXCLUDE_IPS:
            return HttpResponse('<h1>Forbidden</h1>')
        else:
            return view_func(request, *args, **kwargs)
    return inner


# @blocked_ips
def index(request):
    """首页"""
    books = BookInfo.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books/index.html', context)


# @blocked_ips
def ip_test(request):
    return HttpResponse('ip测试')

