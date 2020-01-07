from flask import Flask, render_template


app = Flask(__name__)


@app.route("/macro", methods=["GET"])
def macro():
    return render_template("macro_test.html")


if __name__ == "__main__":
    app.run(debug=True)
