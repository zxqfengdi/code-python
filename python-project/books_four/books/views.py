from django.shortcuts import render, redirect
from books.models import BookInfo
from datetime import date


# 视图函数
def index(request):
    books = BookInfo.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books/index.html', context)


def create(request):
    # 默认增加一条数据到数据库
    book = BookInfo(btitle='流星蝴蝶剑', bpub_date=date(1995, 12, 30))
    book.save()

    # 页面重定向到首页
    return redirect('/books/index/')


def delete(request, book_id):
    # 前端模板删除的请求被URL匹配到，并将删除图书的id传递到此视图函数内
    book = BookInfo.objects.get(id=book_id)
    book.delete()

    # 页面重定向到首页
    return redirect('/books/index/')
