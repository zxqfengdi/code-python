from flask import Flask, session, request, redirect, url_for

app = Flask(__name__)

# 设置安全码
app.config["SECRET_KEY"] = "bafliabfacnoaufhranfoafknikfn165a4sf4klosjfgoi"


@app.route("/login")
def login():
    """登录页"""
    # 获取数据
    username = request.form.get("username")
    password = request.form.get("password")

    # 数据校验
    # 完整性校验
    if not all([username, password]):
        return "数据不完整"

    if username != "yuxi" or password != "199618":
        return "用户名或密码错误"

    # 业务处理：用户名密码正确登录成功，跳转首页(设置一个session信息保存用户登录状态)
    # Django默认将session信息保存在数据库中，flask默认使用安全码混淆session数据将数据存放在cookie中
    if username == "yuxi" and password == "199618":
        session["username"] = "yuxi"
        session["login"] = True

        index_url = url_for("index")
        return redirect(index_url)


@app.route("/index")
def index():
    """首页"""
    return "This is the index page"


if __name__ == "__main__":
    app.run(debug=True)
