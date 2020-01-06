from flask import Flask, request


app = Flask(__name__)


@app.route("/index", methods=["GET"])
def index():
    print("---------视图函数index执行--------")
    return "index page"


@app.before_first_request
def handle_before_first_request():
    """服务器接收第一次请求之前执行"""
    print("-----------handle_first_request------------被执行")


@app.before_request
def handle_before_request():
    """每次请求前均执行"""
    print("-----------handle_before_request----------被执行")


@app.after_request
def handle_after_request(response):
    """每次请求后(视图函数处理后)无异常时执行：需要接收视图函数的返回值进一步处理（response对象）"""
    print("-----------handle_after_request----------被执行")
    return response


@app.teardown_request
def handle_teardown_request(response):
    """每次请求后(视图函数处理后)有无异常均执行：需要接收视图函数的返回值进一步处理（response对象） 出现异常时在非调式模式才执行"""
    print("-----------handle_teardown_request----------被执行")
    return response


if __name__ == "__main__":
    app.run(debug=True)
