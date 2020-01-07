from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# 数据库配置
# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:mysql@127.0.0.1:3306/Flask_test'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  # 设置每次请求结束后会自动提交数据库中的改动(不建议使用)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 设置数据模型类数据和数据库数据同步
# app.config['SQLALCHEMY_ECHO'] = True  # 查询时会显示原始SQL语句


# 使用类设置sqlalchemy
class SqlalchemyConfig(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://yuxi:199618@127.0.0.1:3306/flask_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(SqlalchemyConfig)  # 从类导入配置

# 创建数据库SQLAlchemy工具对象(接收app对象作为参数，使用app.config中数据库相关配置建立数据库连接)
db = SQLAlchemy(app)


# 创建数据模型类(继承自db.Model)
class Role(db.Model):
    """
    角色/身份表：
        name：身份名字
    """
    __tablename__ = "ft_roles"
    id = db.Column(db.Integer, primary_key=True)  # 主键列，整型主键默认为自增
    name = db.Column(db.String(32), unique=True)
    users = db.relationship("User", backref="role")  # 多查一：建立特别属性关联（非真实字段，只用于查询）


class User(db.Model):
    """
    用户表：
        name：用户名
        password：密码
        email：邮箱
    """
    __tablename__ = "ft_users"  # 自定义表名
    # 使用db.Column(字段类型, 字段选项)类将类属性转换为数据库真实字段
    id = db.Column(db.Integer, primary_key=True)  # 主键列，整型主键默认为自增
    name = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey("ft_roles.id"))  # 外键关联(存储另一个表的主键)






if __name__ == "__main__":
    app.run(debug=True)
