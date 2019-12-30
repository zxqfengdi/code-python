from django.db import models


class BookInfo(models.Model):
    """图书模型类"""
    # 图书名称
    btitle = models.CharField(max_length=20, db_column='title')
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

    class Meta:
        db_table = 'bookinfo'
