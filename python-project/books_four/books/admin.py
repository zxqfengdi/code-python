from django.contrib import admin
from books.models import BookInfo, HeroInfo, AreasInfo


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date', 'bread', 'bcomment', 'is_delete']


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hgender', 'hcomment', 'hbook', 'is_delete']


class AreasInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'aname', 'aname_en', 'pid']


# 注册数据模型类
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
admin.site.register(AreasInfo, AreasInfoAdmin)
