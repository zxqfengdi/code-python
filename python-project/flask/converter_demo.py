from flask import Flask
from werkzeug.routing import BaseConverter

# 创建flask实例对象
app = Flask(__name__)


# 路由参数捕获
@app.route("/goods/<int:goods_id>")
def goods_details(goods_id):
    """视图函数定义"""
    return "goods details %d page" % goods_id


# 自定义转换器使用步骤：
# 1. 自定义转换器
class RegexConverter(BaseConverter):
    """自定义转换器类"""
    def __init__(self, url_map, regex):
        """
        :param url_map:当前flask应用实例对象中的路由映射列表
        :param regex:存放传入的正则表达式（flask使用该正则表达式匹配数据）
        """
        super().__init__(url_map)
        self.regex = regex


# 2. 将自定义转换器添加到flask添加到flask应用的转换器字典中
app.url_map.converters['re'] = RegexConverter


# 3. 使用自定义转换器
@app.route('/send/<re(r"1[34578]\d{9}"):mobile>')
def send_sms(mobile):
    return "send sms to %s" % mobile


if __name__ == "__main__":
    app.run(debug=True)  # 启动服务器
