from django.shortcuts import render, redirect
from books.models import BookInfo
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO
import random
# from django.template import loader, RequestContext


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
            # url反向解析
            return redirect(reverse('books:login'))
            # return redirect('/books/login/')  直接写死（硬编码）
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
        # return redirect('/books/change_pwd/')  # 跳转修改密码页面
        return redirect(reverse('books:change_pwd'))  # 跳转修改密码页面
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
    # 获取用户名密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    isRemember = request.POST.get('remember')

    # 获取验证码
    input_verify = request.POST.get('verify_code')
    dest_verify = request.session.get('verifycode')

    # 验证码校验
    if not input_verify == dest_verify:
        # return redirect('/books/login/')
        return redirect(reverse('books:login'))

    # 用户名密码校验
    if username == 'yuxi' and password == '123':
        # 用户名密码正确，跳转到修改密码页面
        response = redirect(reverse('books:change_pwd'))
        # 勾选记住用户名：设置cookie
        if isRemember == 'on':
            response.set_cookie('username', username, max_age=7*24*3600)

        # 记住登录状态
        request.session['isLogin'] = True

        return response
    else:
        # 用户名密码错误，重新回到登录页面
        # return redirect('/books/login/')
        return redirect(reverse('books:login'))

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


def verify_code(request):
    """生成验证码"""
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), 255)
    width = 100
    height = 25

    # 创建图片画布
    im = Image.new('RGB', (width, height), bgcolor)

    # 创建画笔对象
    draw = ImageDraw.Draw(im)

    # 调用画笔的point()函数绘制噪点（增加识别难度）
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))  # 噪点坐标
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))  # 噪点颜色
        draw.point(xy, fill=fill)

    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'

    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]

    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('/Users/yuxi/Library/Fonts/Consolas.ttf', 23)

    # 绘制4个字（fill随机填充颜色）
    draw.text((5, 2), rand_str[0], font=font, fill=(255, random.randrange(0, 255), random.randrange(0, 255)))
    draw.text((25, 2), rand_str[1], font=font, fill=(255, random.randrange(0, 255), random.randrange(0, 255)))
    draw.text((50, 2), rand_str[2], font=font, fill=(255, random.randrange(0, 255), random.randrange(0, 255)))
    draw.text((75, 2), rand_str[3], font=font, fill=(255, random.randrange(0, 255), random.randrange(0, 255)))

    # 释放画笔
    del draw

    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str

    # 内存文件操作（创建BytesIO对象）
    buf = BytesIO()

    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')

    # 将内存中的图片数据返回给浏览器，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')