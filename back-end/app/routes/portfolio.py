from flask import Blueprint, render_template
from app.models import Portfolio

portfolio_bp = Blueprint("portfolio", __name__)


@portfolio_bp.route("/portfolios")
def list_portfolios():
    portfolios = Portfolio.query.all()
    return render_template("portfolios.html", portfolios=portfolios)
