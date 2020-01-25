from flask import Blueprint


# 创建蓝图对象
app_cart = Blueprint("cart", __name__, template_folder="templates")

# 导入views模块，让蓝图知道在views模块中进行了路由注册
from .views import *