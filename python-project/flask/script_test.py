from flask import Flask
from flask_script import Manager  # 启动命令管理类


app = Flask(__name__)

# 创建Manager管理类对象
manager = Manager(app)


@app.route("/index", methods=["GET"])
def index():
    return "index page"


if __name__ == "__main__":
    # app.run(debug=True)
    # 通过管理对象启动flask
    manager.run()
