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
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 自动跟踪


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

    def __repr__(self):
        """自定义对象的显示形式"""
        return "Role:%s" % self.name


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
    password = db.Column(db.String(128), nullable=False)  # nullable：是否可为空
    email = db.Column(db.String(128), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey("ft_roles.id"))  # 外键关联(存储另一个表的主键，类型和主键类型一致)

    def __repr__(self):
        """自定义对象的显示形式"""
        return "User:%s" % self.name


if __name__ == "__main__":
    db.drop_all()  # 清除数据库所有数据表(第一次)
    db.create_all()  # 创建所有表（根据数据模型类）

    # 数据操作
    # 1. 增加数据：创建对象，将对象添加到会话中，会话提交
    role1 = Role(name="admin")  # 以位置参数、关键字参数传参均可
    db.session.add(role1)
    db.session.commit()

    role2 = Role(name="stuff")
    db.session.add(role2)
    db.session.commit()

    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=role1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=role2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=role2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=role1.id)

    # 多条数据可使用db.session.add_all([object_list])
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()

    # 2. 修改数据：
    # 方法1：使用查询操作查询出对象，对象属性重新赋值，然后将对象添加到数据库会话中，提交即可
    # 方法2：查询的同时更新使用update：User.query.filter_by(name='zhang').update({'name':'li'})

    # 2. 查询操作：查询操作使用db.query（常用）或者db.session.query进行，查询条件指明模型类

    # 查询执行器：
    # all()：列表形式返回所有查询结果（模型类对象，可使用对象属性获取数据）
    # get()：根据主键获取一个记录（模型类对象），不存在返回None
    # first()：返回查询结果中的第一条记录（模型类对象），不存在返回None
    # count()：返回查询结果的数量（统计）
    # paginate()：返回一个paginate对象，包含指定范围的查询结果（分页）

    # 查询过滤器：
    # filter_by()：等值过滤器，以关键字参数作为查询条件，多个参数默认为and条件
    # filter()：通用过滤器，以类属性==值的形式作为参数传入，多个参数默认为and（不等：!=）
    # 使用or/not运算需要导入：from sqlalchemy import or_, not_  (使用时使用or_()包括查询条件即可)
    # offset()与limit()：偏移操作即跳过几条数据，从下一条数据开始查询；limit()限制查询出来的数据条数
    # order_by()：需要指明根据那个字段（属性）进行以及排序方式（User.query.order_by(User.id.desc()).all() ）
    # group_by()：分组，使用db.session.query(模型类)进行
    # 分组时使用聚合函数需要导入：from sqlalchemy import func
    # db.session.query(User.role_id, func.count(User.role_id)).group_by(User.role_id).all()

    # 关联查询：（之前在一类中建立了虚拟属性，并使用relationship建立了模型类之间的关联，类似于Django可直接使用虚拟属性获取数据，返回的是对象）
    # 一查多：使用关系属性查询即可
    # 多查一：使用relationship中设置的反向引用属性即可


