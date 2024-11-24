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
