import os
from flask import Blueprint, render_template, send_from_directory

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("home.html")


@main.route("/contact")
def contact():
    return render_template("contact.html")


@main.route("/about")
def about():
    return render_template("about.html")


@main.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join("static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


from .coin import coin_bp
from .chart import chart_bp
from .portfolio import portfolio_bp
from .product import product
