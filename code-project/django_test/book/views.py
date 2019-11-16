from django.shortcuts import render
from django.http import HttpResponse


# 视图函数（URL处理函数）
def index(request):
    # 中间处理，与M，T进行交互
    return HttpResponse('首页')


def center(request):
    return HttpResponse("个人中心")
