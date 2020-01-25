from flask import render_template
from . import app_cart


@app_cart.route("/get_cart")
def get_cart():
    """购物车"""
    context = {
        "info": "购物车页面"
    }
    return render_template("cart.html", **context)
