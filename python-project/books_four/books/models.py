from django.db import models


# 管理器类
class BookInfoManager(models.Manager):
    """图书管理器类"""

    # 改变查询的结果
    def all(self):
        # 1. 调用父类的all方法获得所有结果
        books = super().all()
        # 2. 进行相关处理
        books = books.filter(is_delete=False)
        # 返回处理后结果
        return books

    # 封装方法操作模型类对应的数据表
    def create_book(self, btitle, bpub_date):
        # 创建对象
        book = self.model()
        book.btitle = btitle
        book.bpub_date = bpub_date
        # 保存对象
        book.save()

        return book


# 数据模型类
class BookInfo(models.Model):
    """图书模型类"""
    # 图书名称
    btitle = models.CharField(max_length=20)
    # 出版日期
    bpub_date = models.DateField()
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论数
    bcomment = models.IntegerField(default=0)
    # 删除标记（逻辑删除）
    is_delete = models.BooleanField(default=False)

    # 创建自定义管理器类对象
    objects = BookInfoManager()

    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    """英雄信息类"""
    # 英雄名称
    hname = models.CharField(max_length=20)
    # 英雄性别
    hgender = models.BooleanField(default=True)
    # 备注
    hcomment = models.CharField(max_length=200)
    # 外键关联（关系属性）
    hbook = models.ForeignKey('BookInfo')
    # 删除标记（逻辑删除）
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.hname


class AreasInfo(models.Model):
    """自关联：区域信息类"""
    aname = models.CharField(max_length=30)
    aname_en = models.CharField(max_length=30)
    pid = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.aname


