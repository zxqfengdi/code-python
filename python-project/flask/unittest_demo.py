import unittest
from login import app
import json


class LoginTest(unittest.TestCase):
    """构造单元测试案例"""
    def setUp(self) -> None:
        """单元测试前的准备工作:在单元测试之前进行"""
        # 创建web请求客户端，flask提供
        # 设置flask工作在测试模型下
        # app.config['TESTING'] = True
        app.testing = True

        self.client = app.test_client()

    def test_empty_username_password(self):
        """测试用户名密码不完整情况"""

        # 1. 测试用户名及密码均为空
        # 利用客户端发送web请求，返回结果就是视图函数的响应对象
        ret = self.client.post("/login", data={})
        resp = ret.data  # 从响应对象提取响应体数据(json格式)

        resp = json.loads(resp.decode("utf-8"))  # 转化json格式为对应Python数据类型

        # 断言测试
        self.assertIn("code", resp)  # 判断key code是否在resp中
        self.assertEqual(resp["code"], 1)

        # 2. 测试只传用户名
        ret = self.client.post("/login", data={"username": "fengdi"})
        resp = ret.data  # 从响应对象提取响应体数据(json格式)

        resp = json.loads(resp.decode("utf-8"))  # 转化json格式为对应Python数据类型

        # 断言测试
        self.assertIn("code", resp)  # 判断key code是否在resp中
        self.assertEqual(resp["code"], 1)

        # 3. 测试只传密码
        ret = self.client.post("/login", data={"password": "123456"})
        resp = ret.data  # 从响应对象提取响应体数据(json格式)

        resp = json.loads(resp.decode("utf-8"))  # 转化json格式为对应Python数据类型

        # 断言测试
        self.assertIn("code", resp)  # 判断key code是否在resp中
        self.assertEqual(resp["code"], 1)

    def test_wrong_username_password(self):
        """测试用户名或密码错误"""

        # 1. 测试用户名正确，密码错误
        ret = self.client.post("/login", data={"username": "fengdi", "password": "123456"})
        resp = ret.data
        resp = json.loads(resp.decode("utf-8"))

        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 2)

        # 2. 测试用户名错误，密码正确
        ret = self.client.post("/login", data={"username": "fengdi", "password": "199618"})
        resp = ret.data
        resp = json.loads(resp.decode("utf-8"))

        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 2)

        # 3. 测试用户名密码均错误
        ret = self.client.post("/login", data={"username": "yuxi", "password": "123456"})
        resp = ret.data
        resp = json.loads(resp.decode("utf-8"))

        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 2)


if __name__ == "__main__":
    unittest.main()

