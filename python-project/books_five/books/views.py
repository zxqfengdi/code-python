from django.shortcuts import render, redirect
from books.models import BookInfo
# from django.template import loader, RequestContext
from django.http import HttpResponse


# def index(request):
#     """首页"""
#     # 1. 加载模板文件
#     template = loader.get_template('books/index.html')
#
#     # 2. 填充上下文
#     context = RequestContext(request, {})
#
#     # 3. 渲染模板，生成HTML
#     res_html = template.render(context, request)
#
#     # 4. 返回HttpResponse对象
#     return HttpResponse(res_html)

# 登录状态判断装饰器函数
def login_require(view_func):
    def inner(request, *args, **kwargs):
        if request.session.has_key('isLogin'):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/books/login/')
    return inner


def index(request):
    """首页"""
    context = {}

    return render(request, 'books/index.html', context)


def temp_var(request):
    """模板变量练习"""
    my_dict = {'title': '字典键值'}
    my_list = [1, 2, 3]
    book = BookInfo.objects.get(id=1)

    context = {
        'my_dict': my_dict,
        'my_List': my_list,
        'book': book
    }

    return render(request, 'books/temp_var.html', context)


def temp_tags(request):
    """模板标签"""
    books = BookInfo.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books/temp_tags.html', context)


def temp_filter(request):
    """模板过滤器"""
    books = BookInfo.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books/temp_filter.html', context)


def my_def_filter(request):
    """自定义过滤器"""
    books = BookInfo.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books/my_def_filter.html', context)


def temp_inherit(request):
    """模板继承"""
    return render(request, 'books/child.html', {})


def html_escape(request):
    """HTML转义"""
    context = {
        'content': '<h1>hello world</h1>'
    }
    return render(request, 'books/html_escape.html', context)


def login(request):
    """登录页面"""
    # 判断session属性中是否有isLogin,有则直接跳转首页，没有则进行登录
    if request.session.has_key('isLogin'):
        return redirect('/books/change_pwd/')  # 跳转修改密码页面
    else:
        # 判断请求是否携带cookie：username
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
        else:
            username = ''

        context = {
            'username': username
        }

        return render(request, 'books/login.html', context)


def login_check(request):
    """登录校验"""
    # 1. 获取用户名密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    isRemember = request.POST.get('remember')

    # 2. 数据校验
    if username == 'yuxi' and password == '123':
        # 用户名密码正确，跳转到修改密码页面
        response = redirect('/books/change_pwd/')
        # 勾选记住用户名：设置cookie
        if isRemember == 'on':
            response.set_cookie('username', username, max_age=7*24*3600)

        # 记住登录状态
        request.session['isLogin'] = True

        return response
    else:
        # 用户名密码错误，重新回到登录页面
        return redirect('/books/login/')

# 添加登录状态判断
@login_require
def change_pwd(request):
    """显示修改密码页面"""
    return render(request, 'books/change_pwd.html')


@login_require
def change_pwd_action(request):
    """密码修改后处理"""
    # 获取新密码
    pwd = request.POST.get('change_pwd')
    # 实际开发：拿到新密码，修改数据库存储的密码
    # 返回应答
    return HttpResponse('修改密码成功！')

