from django.contrib import admin
from books.models import BookInfo, HeroInfo


# 自定义模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['btitle', 'bpub_date']


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['hname', 'hgender', 'hcomment', 'hbook']


# 注册数据模型类
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
