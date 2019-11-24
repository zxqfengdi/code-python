from django.db import models


class BookInfo(models.Model):
    """图书模型类"""
    # 图书名称
    btitle = models.CharField(verbose_name='书名', max_length=20, db_column='title')  # 中文列名
    # 出版日期
    bpub_date = models.DateField(verbose_name='出版日期')
    # 阅读量
    bread = models.IntegerField(verbose_name='阅读量', default=0)
    # 评论数
    bcomment = models.IntegerField(verbose_name='评论数', default=0)
    # 删除标记（逻辑删除）
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)

    def __str__(self):
        return self.btitle

    class Meta:
        db_table = 'bookinfo'


class AreasInfo(models.Model):
    """自关联：区域信息类"""
    aname = models.CharField(verbose_name='区域名称', max_length=30)
    aname_en = models.CharField(verbose_name='英文名称', max_length=30)
    pid = models.ForeignKey('self', verbose_name='父级地区', null=True, blank=True)

    def __str__(self):
        return self.aname

    # 方法
    def title(self):
        return self.aname

    title.admin_order_field = 'aname'  # 方法作为显示列可点击排序
    title.short_description = '区域名称'  # 方法作为显示列的别名


class ImageUpload(models.Model):
    pic = models.ImageField(upload_to='books')
