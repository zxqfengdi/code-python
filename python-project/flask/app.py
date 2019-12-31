from flask import Flask, url_for, redirect

# flask应用实例对象：__name__为当前模块名
# flask以当前模块所在目录作为项目的工程目录：static为静态目录、templates为模板目录
app = Flask(__name__)

# 以相对路径指定配置文件
# app.config.from_pyfile("config.cfg")

# 对象方式导入配置文件（类的方式）
# class Config(object):
#     DEBUG = True  # 参数定义为类属性
#
#
# app.config.from_object(Config)

# 直接操作config的字典对象：app.config实际是一个字典对象（参数较少使用）
# app.config["DEBUG"] = True


# 统一路由装饰多个视图函数(若访问方法相同，前者会覆盖后者，建议使用不同访问方式区分)
# @app.route("/index", methods=["POST"])
# def index1():
#     return "hello index1"
#
#
# @app.route("/index", methods=["GET"])
# def index2():
#     return "hello index2"


# 同一视图函数使用多个路由（多个访问路径对应一个视图函数处理）
# @app.route("/index1")
# @app.route("/index2")
# def index():
#     return "hello index"


# url的反向解析
@app.route("/login")
def login():
    index_url = url_for("hello_world")
    return redirect(index_url)  # 重定向依旧使用redirect方法


# 路径和视图函数使用app.route(路径)装饰器进行绑定
@app.route('/')
def hello_world():
    """定义视图函数"""
    return 'Hello World!'


if __name__ == '__main__':
    print(app.url_map)  # 查看所有路由信息
    app.run(debug=True)
