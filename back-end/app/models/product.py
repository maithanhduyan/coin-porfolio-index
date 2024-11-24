from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.extensions import db


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Product '{self.name}'>"
