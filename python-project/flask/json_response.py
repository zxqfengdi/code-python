from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route("/index", methods=["GET"])
def index():
    # 返回json格式数据
    data = {
        "name": "python",
        "age": 18
    }
    # 1. 可使用json.dumps()序列化python对象为对应的json格式数据
    # json_data = json.dumps(data)
    # return json_data, 200, {"Content-Type": "application/json"}

    # 2. 直接返回字典对象会被flask自动转换为json格式
    # return data

    # 3. 如果需要返回字典以外其他json格式的数据，可使用jsonify()函数（序列化任何支持的json格式数据）
    json_data = jsonify(data)
    return json_data


if __name__ == "__main__":
    app.run(debug=True)
