from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    # 接收参数
    username = request.form.get("username")
    password = request.form.get("password")

    a = 1 / 0

    # 参数校验
    # 完整性校验
    if not all([username, password]):
        resp = {
            "code": 1,
            "message": "数据不完整"
        }
        return jsonify(resp)

    # 正确性校验
    if username == "yuxi" and password == "199618":
        resp = {
            "code": 0,
            "message": "登陆成功"
        }
        return jsonify(resp)
    else:
        resp = {
            "code": 2,
            "message": "用户名或密码错误"
        }

        return jsonify(resp)


if __name__ == "__main__":
    app.run(debug=True)