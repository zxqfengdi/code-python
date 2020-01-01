from flask import Flask, make_response


app = Flask(__name__)


@app.route("/index")
def index():
    # 直接返回响应体，头部信息及状态码由flask自己处理
    # return "index page"

    # 1. 返回元组：响应头、状态码(可为自定义状态码)、自定义头部信息（嵌套列表或字典）
    # return "index page", 200, [("language", "python")]
    # return "index page", "666 code description", [("language", "python")]

    # 2. make_response(响应体)函数：返回一个响应体对象（使用其status、headers属性设置状态码及头部信息）
    resp = make_response("index page")
    resp.status = "666 test"  # 状态码（可自定义）
    resp.headers["language"] = "python"

    return resp




if __name__ == "__main__":
    app.run(debug=True)
