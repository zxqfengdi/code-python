from flask import Flask, request, abort, Response


app = Flask(__name__)


@app.route("/index")
def index():
    return "index page"


@app.route("/login", methods=["GET"])
def login():
    # 数据接收
    username = request.form.get("username")
    password = request.form.get("password")

    # 数据检验
    if username != "yuxi" and password != "199618":
        # abort函数可直接终止视图函数执行，并返回给前端特定信息
        # 传递状态码（标准状态码）
        abort(404)

        # 传递响应体信息
        # abort(Response("login failed"))

    return "login success"


# 自定义404错误处理
@app.errorhandler(404)
def handle_404_error(e):
    """
    :param e: 异常错误信息
    :return: 前端页面显示的结果
    """
    return "FILE NOT FOUND:%s" % e


if __name__ == "__main__":
    app.run(debug=True)
