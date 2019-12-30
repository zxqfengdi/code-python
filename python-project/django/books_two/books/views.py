from django.shortcuts import render
from books.models import BookInfo, HeroInfo


# 定义视图函数，处理URL请求
def show_books(request):
    """显示图书信息"""
    books = BookInfo.objects.all()
    context = {
        'books': books
    }

    return render(request, 'books/show_books.html', context)


def book_detail(request, book_id):
    """图书对应的英雄信息"""
    book = BookInfo.objects.get(id=book_id)
    heroes = book.heroinfo_set.all()
    context = {
        'book': book,
        'heroes': heroes
    }

    return render(request, 'books/book_detail.html', context)
