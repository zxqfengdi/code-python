from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from books.models import BookInfo, ImageUpload

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


def show_areas(request):
    """显示区域信息"""
    return HttpResponse('ok')