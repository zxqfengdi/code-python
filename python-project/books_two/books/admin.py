from django.contrib import admin
from books.models import BookInfo, HeroInfo


# 后台管理模型类：自定义显示页面
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['btitle', 'bpub_date']


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['hname', 'hgender', 'hcomment', 'hbook']


# 数据模型类注册（显示在后台页面）
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
