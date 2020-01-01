from flask import Flask, request, make_response


app = Flask(__name__)


@app.route("/set_cookie")
def set_cookie():
    # 1. 创建响应体对象
    resp = make_response("set cookie success")

    # 2. 设置cookie
    resp.set_cookie("username", "fengdi")
    resp.set_cookie("language", "python", max_age=3600)  # cookie过期时间，以s为单位
    # 自定义响应头部信息Set-Cookie字段设置cookie信息
    # resp.headers["Set-Cookie"] = "language=java; Expires=Wed, 01-Jan-2020 08:32:48 GMT; Max-Age=3600; Path=/"

    return resp


@app.route("/get_cookie")
def get_cookie():
    # 获取cookie：request.cookies
    username = request.cookies.get("username")

    return username


@app.route("/delete_cookie")
def delete_cookie():
    # 删除cookie
    # 1. 创建响应体对象
    resp = make_response("delete cookie success")

    # 2. 删除cookie（并非真正删除，而是设置过期时间）
    resp.delete_cookie("username")

    return resp


if __name__ == "__main__":
    app.run(debug=True)
