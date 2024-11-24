from flask import Blueprint, render_template
from app.models import Product

product = Blueprint('product', __name__)

@product.route('/product')
def product_list():
    products = Product.query.all()
    return render_template('product.html', products=products)
