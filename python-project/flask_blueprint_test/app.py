from flask import Flask
from users import app_users  # 导入users模块的抽象形式即蓝图对象
from cart import app_cart  # 从cart包中的__init__文件导入蓝图对象

app = Flask(__name__)

# 注册蓝图对象，将users模块的路由绑定到app对象上
app.register_blueprint(app_users, url_prefix="/users")
app.register_blueprint(app_cart, url_prefix="/cart")


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
