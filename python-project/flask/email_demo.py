from flask import Flask, render_template, redirect, url_for
from flask_mail import Mail, Message
from flask_script import Manager

app = Flask(__name__)

# 邮件配置
app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.163.com',
    MAIL_PROT=25,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='zxqfengdi@163.com',
    MAIL_PASSWORD='Zxq199618',
)

manager = Manager(app)  # 项目管理器对象
mail = Mail(app)  # 邮件发送对象


@app.route("/", methods=["GET"])
def index():
    context = {
        "info": "欢迎来到首页！！"
    }

    return render_template("send_mail.html", **context)


@app.route("/send_mail", methods=['GET'])
def send_mail():
    """邮件发送"""
    msg = Message("flask欢迎消息", sender="zxqfengdi@163.com", recipients=["zxqfengdi@163.com"])
    # msg.body = "测试邮件"  # 邮件内容
    msg.html = "'<h3>欢迎您成为天天生鲜注册会员！</h3>请点击以下链接激活账户：<a href='#'>激活</a>"  # html消息

    mail.send(msg)  # 发送邮件

    return redirect(url_for("index"))


if __name__ == "__main__":
    manager.run()

