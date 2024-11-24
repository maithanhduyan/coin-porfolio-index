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

    from .routes.chart import chart_bp

    app.register_blueprint(chart_bp)

    return app


app = create_app()

from .cli_command import create_db, seed_db

if __name__ == "__main__":
    app.run(debug=True)
