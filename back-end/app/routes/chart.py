# chart.py

from flask import Blueprint, render_template

chart_bp = Blueprint("chart", __name__)


@chart_bp.route("/chart")
def show_chart():
    return render_template("chart.html")
