from django.contrib import admin
from books.models import BookInfo, AreasInfo, ImageUpload


# 在一类的编辑页面嵌入关联模型的编辑选项
class AreaStackedInline(admin.StackedInline):
    model = AreasInfo  # 关联的模型类
    extra = 2  # 额外编辑个数


class BookInfoAdmin(admin.ModelAdmin):
    actions_on_top = True  # 操作栏位置
    actions_on_bottom = True  # 操作栏位置
    list_per_page = 20  # 每页显示数量
    search_fields = ['btitle']  # 搜索框
    list_filter = ['btitle']  # 过滤栏
    list_display = ['btitle', 'bpub_date', 'bread', 'bcomment', 'is_delete']  # 显示列
    fields = ['btitle', 'bpub_date', 'bcomment', 'bread', 'is_delete']  # 显示顺序


class AreasInfoAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    list_per_page = 20
    search_fields = ['aname']
    list_filter = ['pid']
    list_display = ['aname', 'aname_en', 'pid', 'title']  # 显示列（方法作为列）
    inlines = [AreaStackedInline]


# 注册数据模型类
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(AreasInfo, AreasInfoAdmin)
admin.site.register(ImageUpload)
