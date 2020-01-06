from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/index", methods=["GET"])
def index():
    """首页"""
    languages = ["python", "java", "javascript"]
    num = list(range(10))

    context = {
        "name": "fengdi",
        "age": 18,
        "languages": languages,
        "num": num
    }
    # 1. 直接使用关键字参数传入
    # return render_template("index.html", name="fengdi", age=18, language="python")

    # 2. 使用**解包字典传入
    return render_template("index.html", **context)


# 自定义过滤器
# 1. app.add_template_filter()方法实现
def list_step_2(lst):
    """以步长2取出列表中数据"""
    return lst[::2]


app.add_template_filter(list_step_2, "li2")  # 注册自定义过滤器：添加自定义过滤器到当前应用实例的过滤器中


# 2. 以app.template_filter装饰器实现，传入过滤器名字即可
@app.template_filter("li3")
def list_step_3(lst):
    """以步长3取出列表中数据"""
    return lst[::3]


if __name__ == "__main__":
    app.run(debug=True)

