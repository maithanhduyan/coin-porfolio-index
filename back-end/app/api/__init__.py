from flask import Blueprint, jsonify
from app.extensions import db
from app.models import User
from app.models.product import Product

api = Blueprint("api", __name__)


@api.route("/api/healcheck")
def healthcheck():
    return jsonify({"status": "OK"})


@api.route("/api/data")
def get_data():
    data = "Xin chào từ Flask!"
    return jsonify({"message": data})


@api.route("/api/users")
def get_users():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return jsonify({"message": users})


@api.route("/api/products")
def get_products():
    products = Product.query.all()
    product_list = [{"id": p.id, "name": p.name} for p in products]
    return jsonify(product_list)
