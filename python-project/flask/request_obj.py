from flask import Flask, request


app = Flask(__name__)


@app.route("/index", methods=["GET", "POST"])
def index():
    # request对象包含前端请求所有信息
    # request.form包含请求体中的表单格式数据（类字典对象）
    name = request.form.get("name")
    age = request.form.get("age")
    name_list = request.form.getlist("name")

    # request.data包含请求体中的非表单格式数据（二进制字符串）
    print(request.data.decode("utf-8"))

    # request.args包含请求体中的查询字符串（请求路径中?后面的键值对数据）
    city = request.args.get("city")

    return "name=%s, age=%s, city=%s, namelist=%s" % (name, age, city, name_list)


if __name__ == "__main__":
    app.run(debug=True)
