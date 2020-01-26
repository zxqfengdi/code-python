import unittest
from book_demo import Author, app, db


class DatabaseTest(unittest.TestCase):
    """数据库测试"""
    def setUp(self) -> None:
        app.testing = True
        app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://yuxi:199618@127.0.0.1:3306/test0'  # 使用隔离的测试数据库
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

        # 创建数据表
        db.create_all()

    def tearDown(self) -> None:
        """所有测试执行完后进行，通常用来进行清理操作"""
        db.session.remove()  # 清除数据库连接
        db.drop_all()  # 删除测试创建的数据表

    def test_add_author(self):
        """测试添加作者的数据库操作"""
        author = Author(name="小丸子", email="zxqfengdi@163.com")
        db.session.add(author)
        db.session.commit()

        result_author = Author.query.filter_by(name="小丸子").first()
        self.assertIsNotNone(result_author)


