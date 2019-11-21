from django.shortcuts import render
from books.models import BookInfo
# from django.template import loader, RequestContext
# from django.http import HttpResponse


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