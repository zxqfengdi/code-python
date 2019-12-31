from flask import Flask, request
from werkzeug import secure_filename

app = Flask(__name__)


@app.route("/file", methods=["POST"])
def file_upload():
    image = request.files.get("image")

    if image is None:
        return "文件未上传"

    # 保存文件到本地(使用save方法保存)
    # with open("./demo.jpg", "wb") as f2:
    #     f2.write(image.read())

    # 获取上传文件的文件名(建议传递给Werkzeug提供的secure_filename()函数)
    image_name = secure_filename(image.filename)
    print(image_name)
    image.save("./" + image_name)

    return "文件上传成功！"


if __name__ == "__main__":
    app.run(debug=True)
