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
