from flask import Blueprint, render_template
from app.models import Coin

coin_bp = Blueprint("coin", __name__)


@coin_bp.route("/coins")
def list_coins():
    coins = Coin.query.order_by(Coin.name).all()
    return render_template("coins.html", coins=coins)


@coin_bp.route("/coins/<int:coin_id>")
def coin_detail(coin_id):
    coin = Coin.query.get_or_404(coin_id)
    return render_template("coin_detail.html", coin=coin)
