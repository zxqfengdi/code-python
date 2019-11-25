from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.core.paginator import Paginator
from books.models import BookInfo, ImageUpload, AreasInfo

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


def show_upload(request):
    """显示上传图片页面"""
    return render(request, 'books/upload_img.html')


def upload_handle(request):
    """上传图片处理"""
    # 1. 获取上传文件的处理对象
    image = request.FILES['image']
    # image.name  上传文件的名字
    # image.chunks()方法  上传文件的内容

    # 2. 创建一个文件
    save_path = '%s/books/%s' % (settings.MEDIA_ROOT, image.name)
    with open(save_path, 'wb') as f:
        # 3. 获取上传的文件写入到创建的文件中
        for content in image.chunks():
            f.write(content)
    # 4. 保存上传文件的记录（数据库中添加记录）
    ImageUpload.objects.create(pic='books/%s' % image.name)

    # 5. 返回
    return HttpResponse('ok')


# 分页：前端页面应传递需求页面的页码
def show_areas(request, pageindex):
    """显示区域信息"""
    # 1. 查出所有的省级地区
    areas = AreasInfo.objects.filter(pid__isnull=True)

    # 2. 分页：创建paginator对象
    paginator = Paginator(areas, 10)
    # print(paginator.count)  # 查询集中的总个数
    # print(paginator.num_pages)  # 分页后的总页数
    # print(paginator.page_range)  # 分页后的页面页面列表，从1开始

    # 对前端点击传递的页码做判断，默认为第一页
    if pageindex == '':
        pageindex = 1

    # 3. 创建Page类对象
    page = paginator.page(int(pageindex))  # page方法接收页面作为参数，返回对应页的查询集
    # print(page.number)  # 当前页的页码

    context = {
        'page': page
    }

    return render(request, 'books/show_areas.html', context)


def areas(request):
    """省市县选择案例页面"""
    return render(request, 'books/areas.html')


def province(request):
    """处理ajax请求获取所有省级地区的信息"""
    provinces = AreasInfo.objects.filter(pid__isnull=True)

    # 对象不能直接转换为json数据格式，需要自己拼接转换:aname, id
    areas_list = []
    for area in provinces:
        areas_list.append((area.id, area.aname))

    # 返回数据
    context = {
        'provinces': areas_list
    }

    return JsonResponse(context)


def city(request, pid):
    """市级地区"""
    cities = AreasInfo.objects.filter(pid__id=pid)

    areas_list = []
    for area in cities:
        areas_list.append((area.id, area.aname))

    context = {
        'cities': areas_list
    }

    return JsonResponse(context)


def dis(request, cid):
    """县级地区"""
    dises = AreasInfo.objects.filter(pid__id=cid)

    areas_list = []
    for area in dises:
        areas_list.append((area.id, area.aname))

    context = {
        'dises': areas_list
    }

    return JsonResponse(context)