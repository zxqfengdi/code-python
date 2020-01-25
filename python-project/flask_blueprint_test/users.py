from flask import Blueprint


# 创建蓝图对象(用于存储在app对象上执行的操作，主要是路由注册相关)
app_users = Blueprint("users", __name__)


# 定义视图函数并使用蓝图对象注册路由（存储路由操作）
@app_users.route("/register")
def register():
    return "欢迎来到注册页面！！！"

