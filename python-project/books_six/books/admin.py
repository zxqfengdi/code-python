from django.contrib import admin
from books.models import BookInfo, AreasInfo


class BookInfoAdmin(admin.ModelAdmin):
    actions_on_top = True  # 操作栏位置
    actions_on_bottom = True  # 操作栏位置
    list_per_page = 20  # 每页显示数量
    search_fields = ['btitle']  # 搜索框
    list_filter = ['btitle']  # 过滤栏
    list_display = ['id', 'btitle', 'bpub_date', 'bread', 'bcomment', 'is_delete']  # 显示列


class AreasInfoAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    list_per_page = 20
    search_fields = ['aname']
    list_filter = ['pid']
    list_display = ['id', 'aname', 'aname_en', 'pid', 'title']  # 显示列（方法作为列）


# 注册数据模型类
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(AreasInfo, AreasInfoAdmin)
