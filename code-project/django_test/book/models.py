from django.db import models


# 数据模型类
class BookInfo(models.Model):
    """图书类"""
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()

    # 个性化显示数据print函数相关
    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    """英雄类"""
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    hcomment = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo', on_delete=False)

    def __str__(self):
        return self.hname
