from flask import Flask

# flask应用实例对象：__name__为当前模块名
# flask以当前模块所在目录作为项目的工程目录：static为静态目录、templates为模板目录
app = Flask(__name__)


# 路径和视图函数使用app.route(路径)装饰器进行绑定
@app.route('/')
def hello_world():
    """定义视图函数"""
    a = 1 / 0
    return 'Hello World!'


# 以相对路径指定配置文件
# app.config.from_pyfile("config.cfg")

# 对象方式导入配置文件（类的方式）
# class Config(object):
#     DEBUG = True  # 参数定义为类属性
#
#
# app.config.from_object(Config)

# 直接操作config的字典对象：app.config实际是一个字典对象（参数较少使用）
app.config["DEBUG"] = True


if __name__ == '__main__':
    app.run()
