from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)  # flask程序实例对象


# 创建数据库连接及配置
class SqlalchemyConfig(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://yuxi:199618@127.0.0.1:3306/flask_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 自动跟踪


app.config.from_object(SqlalchemyConfig)
app.config['SECRET_KEY'] = "ilabnlrhfwbiufbhabfaiufgbhi"
db = SQLAlchemy(app)  # 数据库管理对象

manager = Manager(app)  # 创建flask脚本管理对象

migrate = Migrate(app, db)  # 创建数据库迁移工具对象

manager.add_command('db', MigrateCommand)  # 向manager对象添加数据库操作命令


# 创建数据模型类
class Author(db.Model):
    """作者"""
    __tablename__ = "bk_authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(64))
    books = db.relationship("Book", backref="author")  # 虚拟字段，方便查询，反向引用（非真实存在）


class Book(db.Model):
    """书籍"""
    __tablename__ = "bk_books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey("bk_authors.id"))  # 存储作者id（外键关联）


# 表单模型类
class BookInfoForm(FlaskForm):
    author = StringField(label="作者", validators=[DataRequired("作者不为空")])
    book = StringField(label="书籍", validators=[DataRequired("书籍不为空")])

    submit = SubmitField(label="提交")


# 视图函数
@app.route("/index", methods=['GET', 'POST'])
def index():
    form = BookInfoForm()  # 根据表单模型类创建表单对象传递到前端页面使用相关属性

    if form.validate_on_submit():
        # 获取表单提交信息
        author_name = form.author.data
        book_name = form.book.data

        # 添加信息到数据库
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        book = Book(name=book_name, author_id=author.id)
        # book = Book(name=book_name, author=author)
        db.session.add(book)
        db.session.commit()

    # 从数据库查询所有作者信息
    authors = Author.query.all()

    context = {
        'authors': authors,
        'form': form
    }

    return render_template("bookkinfo.html", **context)


# @app.route("/add", methods=["POST"])
# def add():
#     """添加书籍信息"""
#     # 获取表单提交信息
#     author_name = request.form.get("author")
#     book_name = request.form.get("book")
#
#     # 添加信息到数据库
#     author = Author(name=author_name)
#     db.session.add(author)
#     db.session.commit()
#
#     book = Book(name=book_name, author_id=author.id)
#     db.session.add(book)
#     db.session.commit()
#
#     # 返回页面响应：当前页面刷新
#     index_url = url_for("index")
#     return redirect(index_url)


@app.route("/delete/<int:book_id>", methods=['GET'])
def delete(book_id):
    # 根据URL传递的书籍id删除书籍
    book = Book.query.get(book_id)

    # 删除书籍
    db.session.delete(book)
    db.session.commit()

    # 返回页面响应：页面刷新
    index_url = url_for("index")
    return redirect(index_url)


if __name__ == "__main__":
    # db.create_all()
    #
    # # 添加数据
    # au_xi = Author(name='我吃西红柿')
    # au_qian = Author(name='萧潜')
    # au_san = Author(name='唐家三少')
    # db.session.add_all([au_xi, au_qian, au_san])
    # db.session.commit()
    #
    # bk_xi = Book(name='吞噬星空', author_id=au_xi.id)
    # bk_xi2 = Book(name='寸芒', author_id=au_qian.id)
    # bk_qian = Book(name='飘渺之旅', author_id=au_qian.id)
    # bk_san = Book(name='冰火魔厨', author_id=au_san.id)
    # db.session.add_all([bk_qian, bk_san, bk_xi, bk_xi2])
    # db.session.commit()

    # app.run(debug=True)

    # 脚本形式启动
    manager.run()
