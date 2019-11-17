from django.db import models


# 数据模型类（对应数据表）
class BookInfo(models.Model):
    """图书信息类"""
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()

    # 自定义显示形式
    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    """英雄信息类"""
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    hcomment = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo')

    def __str__(self):
        return self.hname
