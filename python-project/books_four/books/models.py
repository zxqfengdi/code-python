from django.db import models


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

