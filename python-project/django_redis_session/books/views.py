from django.shortcuts import render
from django.http import HttpResponse


def set_session(request):
    """设置session"""
    request.session['username'] = 'yuxi'
    request.session['age'] = 18

    return HttpResponse("设置session")


def get_session(request):
    """获取session"""
    username = request.session.get('username')
    age = request.session.get('age')

    return HttpResponse(username + ':' + str(age))
