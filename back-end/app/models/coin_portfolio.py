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
