from django.shortcuts import render
from books.models import BookInfo, HeroInfo


# 视图函数
def show_books(request):
    books = BookInfo.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books/show_books.html', context)


def book_detail(request, book_id):
    book = BookInfo.objects.get(id=book_id)
    heroes = book.heroinfo_set.all()
    context = {
        'book': book,
        'heroes': heroes
    }
    return render(request, 'books/book_detail.html', context)
