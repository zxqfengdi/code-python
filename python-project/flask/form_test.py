from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm  # 导入扩展表单父类
from wtforms import StringField, PasswordField, SubmitField  # 导入表单使用的字段类型
from wtforms.validators import DataRequired, EqualTo  # 导入表单数据验证器

app = Flask(__name__)

app.config["SECRET_KEY"] = "IJALBHFIAGBBWFUDVBALIUD123"


# 定义表单模型类
class RegisterForm(FlaskForm):
    """自定义注册页面表单模型类"""
    # 和Django类似，每个字段都是一个Field类的实例
    # 可选参数：label表示表单控件label属性、validators表示接收的验证器
    username = StringField(label="用户名", validators=[DataRequired("用户名不能为空")])
    password = PasswordField(label="密码", validators=[DataRequired("密码不能为空")])
    # DataRequired：数据必须填写，不可为空（可传入一个参数作为条件不满足情况下的提示信息：字符串）
    # EqualTo：与另一个字段进行比较，第一个参数为比较的字段，第二个参数为提示信息
    password2 = PasswordField(label="确认密码", validators=[DataRequired("确认密码不能为空"), EqualTo("password", "两次输入密码不一致")])

    submit = SubmitField(label="提交")


@app.route("/register", methods=["GET", "POST"])
def register():
    """注册页面"""
    # 使用创建的表单类创建表单对象（表单对象可传递到前端模板页面使用其相关属性）
    # 如果是Post方式提交数据，flask会将提交的数据存储在form对象内
    form = RegisterForm()

    # 2. 数据校验: validate_on_submit-->表单数据满足验证器要求则返回True否则返回False
    if form.validate_on_submit():
        # 验证合格
        # 提取数据(form.属性名返回一个对象，使用data属性提取数据)
        username = form.username.data
        password = form.password.data
        password2 = form.password2.data

        print(username, password, password2)
        return redirect(url_for("index"))  # 验证成功重定向到首页

    return render_template("register.html", form=form)


@app.route("/index", methods=["GET"])
def index():
    return "index page"


if __name__ == "__main__":
    app.run(debug=True)
