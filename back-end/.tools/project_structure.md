# Cấu trúc Dự án như sau:

```
├── .env
├── app
│   ├── __init__.py
│   ├── ai
│   │   ├── __init__.py
│   │   ├── architect.py
│   │   ├── connection.py
│   │   ├── group.py
│   │   ├── layer.py
│   │   ├── network.py
│   │   └── node.py
│   ├── api
│   │   └── __init__.py
│   ├── app.py
│   ├── cli_command.py
│   ├── config.py
│   ├── extensions.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── coin.py
│   │   ├── coin_portfolio.py
│   │   ├── portfolio.py
│   │   ├── product.py
│   │   └── user.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── coin.py
│   │   ├── portfolio.py
│   │   └── product.py
│   ├── templates
│   │   ├── about.html
│   │   ├── base.html
│   │   ├── coin_detail.html
│   │   ├── coins.html
│   │   ├── contact.html
│   │   ├── home.html
│   │   ├── portfolios.html
│   │   └── product.html
│   └── test
│       └── test_xor.py
└── requirements.txt
```

# Danh sách Các Tệp Dự án:

## d:\Project\coin-porfolio-index\back-end\app\app.py

```
from flask import Flask
from app.config import Config
from app.extensions import db as database
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    # Load configuration
    app.config.from_object(Config)

    # Initialize extensions
    database.init_app(app)

    # Xóa bộ nhớ đệm
    app.jinja_env.cache = {}

    CORS(app)

    # Register blueprints
    from .api import api

    app.register_blueprint(api)

    from .routes import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from .routes import product as product_blueprint

    app.register_blueprint(product_blueprint)

    from .routes.coin import coin_bp

    app.register_blueprint(coin_bp)

    from .routes.portfolio import portfolio_bp

    app.register_blueprint(portfolio_bp)

    return app


app = create_app()

from .cli_command import create_db, seed_db

if __name__ == "__main__":
    app.run(debug=True)

```

 ## d:\Project\coin-porfolio-index\back-end\app\cli_command.py

```
from .app import app
from app.extensions import db as database


@app.cli.command("create-db")
def create_db():
    """Create the database."""
    database.create_all()
    print("Database tables created.")


@app.cli.command("seed-db")
def seed_db():
    """Seed the database with sample data."""
    from app.models import Product, User, Portfolio, Coin, CoinPortfolio

    product1 = Product(name="Product1")
    product2 = Product(name="Product2")

    database.session.add_all([product1, product2])

    # List of coins to add
    coin_data = [
        {"name": "Bitcoin", "symbol": "BTC"},
        {"name": "Ethereum", "symbol": "ETH"},
        {"name": "Cardano", "symbol": "ADA"},
        {"name": "Solana", "symbol": "SOL"},
        {"name": "Dogecoin", "symbol": "DOGE"},
        {"name": "Polygon", "symbol": "MATIC"},
        {"name": "Polkadot", "symbol": "DOT"},
        {"name": "Litecoin", "symbol": "LTC"},
        {"name": "Shiba Inu", "symbol": "SHIB"},
        {"name": "Tron", "symbol": "TRX"},
        {"name": "Avalanche", "symbol": "AVAX"},
        {"name": "Uniswap", "symbol": "UNI"},
        {"name": "Cosmos", "symbol": "ATOM"},
        {"name": "Chainlink", "symbol": "LINK"},
        {"name": "Monero", "symbol": "XMR"},
        {"name": "Ethereum Classic", "symbol": "ETC"},
        {"name": "Bitcoin Cash", "symbol": "BCH"},
        {"name": "Stellar", "symbol": "XLM"},
        {"name": "Filecoin", "symbol": "FIL"},
        {"name": "Lido DAO", "symbol": "LDO"},
        {"name": "Aptos", "symbol": "APT"},
        {"name": "NEAR Protocol", "symbol": "NEAR"},
        {"name": "ApeCoin", "symbol": "APE"},
        {"name": "VeChain", "symbol": "VET"},
        {"name": "Algorand", "symbol": "ALGO"},
        {"name": "EOS", "symbol": "EOS"},
        {"name": "Fantom", "symbol": "FTM"},
        {"name": "Decentraland", "symbol": "MANA"},
        {"name": "Aave", "symbol": "AAVE"},
        {"name": "The Graph", "symbol": "GRT"},
    ]

    # Insert coins
    coins = []
    for coin_info in coin_data:
        coin = Coin(name=coin_info["name"], symbol=coin_info["symbol"])
        coins.append(coin)
        database.session.add(coin)

    # Create sample users
    user1 = User(username="user1", email="user1@example.com")
    user2 = User(username="user2", email="user2@example.com")

    database.session.add_all([user1, user2])

    # Create sample portfolios
    portfolio1 = Portfolio(name="Portfolio 1", user=user1)
    portfolio2 = Portfolio(name="Portfolio 2", user=user1)
    portfolio3 = Portfolio(name="Portfolio 3", user=user2)

    database.session.add_all([portfolio1, portfolio2, portfolio3])

    # Assign coins to portfolios (sample data)
    cp1 = CoinPortfolio(portfolio=portfolio1, coin=coins[0])  # Bitcoin in Portfolio 1
    cp2 = CoinPortfolio(portfolio=portfolio1, coin=coins[1])  # Ethereum in Portfolio 1
    cp3 = CoinPortfolio(portfolio=portfolio2, coin=coins[2])  # Cardano in Portfolio 2
    cp4 = CoinPortfolio(portfolio=portfolio3, coin=coins[3])  # Solana in Portfolio 3
    cp5 = CoinPortfolio(portfolio=portfolio3, coin=coins[4])  # Dogecoin in Portfolio 3

    database.session.add_all([cp1, cp2, cp3, cp4, cp5])

    database.session.commit()
    print("Sample data inserted.")

```

 ## d:\Project\coin-porfolio-index\back-end\app\config.py

```
# config.py

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    # default: 'your-secret-key'
    SECRET_KEY = os.environ.get("SECRET_KEY", "your-secret-key")

    SQLALCHEMY_DATABASE_URI = "sqlite:///coin.db"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Thêm các cấu hình khác nếu cần

```

 ## d:\Project\coin-porfolio-index\back-end\app\extensions.py

```
# extensions.py

# db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

```

 ## d:\Project\coin-porfolio-index\back-end\app\__init__.py

```

```

 ## d:\Project\coin-porfolio-index\back-end\app\ai\architect.py

```
# architect.py

from .network import Network
from .layer import Layer


class Architect:
    @staticmethod
    def create_feedforward(
        input_size,
        hidden_sizes,
        output_size,
        activation_function=None,
        activation_derivative=None,
    ):
        network = Network()
        # Tạo layer đầu vào
        input_layer = Layer(input_size, activation_function, activation_derivative)
        network.add_layer(input_layer)
        # Tạo các layer ẩn
        for size in hidden_sizes:
            hidden_layer = Layer(size, activation_function, activation_derivative)
            network.add_layer(hidden_layer)
        # Tạo layer đầu ra
        output_layer = Layer(output_size, activation_function, activation_derivative)
        network.add_layer(output_layer)
        return network

```

 ## d:\Project\coin-porfolio-index\back-end\app\ai\connection.py

```
# connection.py


class Connection:
    def __init__(self, from_node, to_node, weight=1.0):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def propagate(self, value):
        # Truyền giá trị từ node nguồn đến node đích
        self.to_node.input_value += value * self.weight

```

 ## d:\Project\coin-porfolio-index\back-end\app\ai\group.py

```
# group.py


class Group:
    def __init__(self, elements):
        self.elements = elements

    def activate(self):
        for element in self.elements:
            element.activate()

```

 ## d:\Project\coin-porfolio-index\back-end\app\ai\layer.py

```
# layer.py

from .node import Node


class Layer:
    def __init__(self, num_nodes, activation_function=None, activation_derivative=None):
        self.nodes = [
            Node(activation_function, activation_derivative) for _ in range(num_nodes)
        ]

    def connect_to(self, next_layer):
        from .connection import Connection

        for node in self.nodes:
            for next_node in next_layer.nodes:
                connection = Connection(node, next_node)
                node.add_connection(connection)

```

 ## d:\Project\coin-porfolio-index\back-end\app\ai\network.py

```
# network.py


class Network:
    def __init__(self):
        self.layers = []

    def add_layer(self, layer):
        if self.layers:
            self.layers[-1].connect_to(layer)
        self.layers.append(layer)

    def feed_forward(self, input_values):
        # Reset input cho tất cả các node
        for layer in self.layers:
            for node in layer.nodes:
                node.reset_input()

        # Thiết lập giá trị đầu vào cho layer đầu tiên
        for i, node in enumerate(self.layers[0].nodes):
            node.input_value = input_values[i]
            node.activate()

        # Kích hoạt các layer tiếp theo
        for layer in self.layers[1:]:
            for node in layer.nodes:
                node.activate()

    def backpropagate(self, target_values, learning_rate):
        # Tính delta cho layer đầu ra
        output_layer = self.layers[-1]
        for i, node in enumerate(output_layer.nodes):
            error = target_values[i] - node.output_value
            node.delta = error * node.activation_derivative(node.output_value)

        # Tính delta cho các layer ẩn
        for l in reversed(range(len(self.layers) - 1)):
            current_layer = self.layers[l]
            next_layer = self.layers[l + 1]
            for i, node in enumerate(current_layer.nodes):
                error = sum(
                    [conn.weight * conn.to_node.delta for conn in node.connections]
                )
                node.delta = error * node.activation_derivative(node.output_value)

        # Cập nhật trọng số
        for layer in self.layers[:-1]:
            for node in layer.nodes:
                for conn in node.connections:
                    conn.weight += (
                        learning_rate * node.output_value * conn.to_node.delta
                    )

    def train(self, training_data, learning_rate, epochs):
        for epoch in range(epochs):
            for input_values, target_values in training_data:
                self.feed_forward(input_values)
                self.backpropagate(target_values, learning_rate)

    def get_output(self):
        return [node.output_value for node in self.layers[-1].nodes]

```

 ## d:\Project\coin-porfolio-index\back-end\app\ai\node.py

```
# node.py


class Node:
    def __init__(self, activation_function=None, activation_derivative=None):
        self.input_value = 0.0
        self.output_value = 0.0
        self.activation_function = activation_function
        self.activation_derivative = activation_derivative
        self.connections = []
        self.delta = 0.0  # Dùng để lưu trữ lỗi trong quá trình backpropagation

    def activate(self):
        if self.activation_function:
            self.output_value = self.activation_function(self.input_value)
        else:
            self.output_value = self.input_value
        for conn in self.connections:
            conn.propagate(self.output_value)

    def add_connection(self, connection):
        self.connections.append(connection)

    def reset_input(self):
        self.input_value = 0.0

```

 ## d:\Project\coin-porfolio-index\back-end\app\ai\__init__.py

```


```

 ## d:\Project\coin-porfolio-index\back-end\app\api\__init__.py

```
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

```

 ## d:\Project\coin-porfolio-index\back-end\app\models\coin.py

```
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.extensions import db


class Coin(db.Model):
    __tablename__ = "coins"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    symbol: Mapped[str] = mapped_column(String(10), nullable=False)

    # Relationship to CoinPortfolio (association table)
    coin_portfolios = relationship("CoinPortfolio", back_populates="coin")

```

 ## d:\Project\coin-porfolio-index\back-end\app\models\coin_portfolio.py

```
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.extensions import db


class CoinPortfolio(db.Model):
    __tablename__ = "coin_portfolios"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # Foreign keys
    portfolio_id: Mapped[int] = mapped_column(Integer, ForeignKey("portfolios.id"))
    coin_id: Mapped[int] = mapped_column(Integer, ForeignKey("coins.id"))

    # Relationships
    portfolio = relationship("Portfolio", back_populates="coin_portfolios")
    coin = relationship("Coin", back_populates="coin_portfolios")

```

 ## d:\Project\coin-porfolio-index\back-end\app\models\portfolio.py

```
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.extensions import db


class Portfolio(db.Model):
    __tablename__ = "portfolios"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    # Foreign key to User
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="portfolios")

    # Relationship to CoinPortfolio (association table)
    coin_portfolios = relationship("CoinPortfolio", back_populates="portfolio")

```

 ## d:\Project\coin-porfolio-index\back-end\app\models\product.py

```
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.extensions import db


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Product '{self.name}'>"

```

 ## d:\Project\coin-porfolio-index\back-end\app\models\user.py

```
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.extensions import db


class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(100), unique=True)
    email: Mapped[str] = mapped_column(String(120), unique=True)

    # Relationship to Portfolio
    portfolios = relationship("Portfolio", back_populates="user")

```

 ## d:\Project\coin-porfolio-index\back-end\app\models\__init__.py

```
from .user import User
from .product import Product
from .coin import Coin
from .portfolio import Portfolio
from .coin_portfolio import CoinPortfolio

```

 ## d:\Project\coin-porfolio-index\back-end\app\routes\coin.py

```
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

```

 ## d:\Project\coin-porfolio-index\back-end\app\routes\portfolio.py

```
from flask import Blueprint, render_template
from app.models import Portfolio

portfolio_bp = Blueprint("portfolio", __name__)


@portfolio_bp.route("/portfolios")
def list_portfolios():
    portfolios = Portfolio.query.all()
    return render_template("portfolios.html", portfolios=portfolios)

```

 ## d:\Project\coin-porfolio-index\back-end\app\routes\product.py

```
from flask import Blueprint, render_template
from app.models import Product

product = Blueprint('product', __name__)

@product.route('/product')
def product_list():
    products = Product.query.all()
    return render_template('product.html', products=products)

```

 ## d:\Project\coin-porfolio-index\back-end\app\routes\__init__.py

```
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


# Import and register the coin blueprint
from .coin import coin_bp

# Import the portfolio blueprint
from .portfolio import portfolio_bp
from .product import product

```

 ## d:\Project\coin-porfolio-index\back-end\app\test\test_xor.py

```
from ai.architect import Architect

print("hello")

```

 