from django.db import models
from db.base_model import BaseModel
from django.contrib.auth.models import AbstractUser


class User(AbstractUser, BaseModel):
    """用户模型类"""

    class Meta:
        db_table = 'df_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class AddressManager(models.Manager):
    """地址模型管理器类"""
    # 使用场景1：改变默认查询方法的结果集
    # 使用场景2：封装自己的方法操作数据表
    def get_default_address_obj(self, user):
        try:
            address = self.get(user=user, is_default=True)
        except self.model.DoesNotExist:
            address = None

        return address


class Address(BaseModel):
    """地址模型类"""
    user = models.ForeignKey('User', verbose_name='所属用户')
    receiver = models.CharField(max_length=20, verbose_name='收件人')
    addr = models.CharField(max_length=256, verbose_name='收件地址')
    zip_code = models.CharField(max_length=6, null=True, verbose_name='邮政编码')
    phone = models.CharField(max_length=11, verbose_name='联系电话')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')

    # 创建自定义模型管理器类的对象（默认是models.Model.objects）
    objects = AddressManager()

    class Meta:
        db_table = 'df_address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name
