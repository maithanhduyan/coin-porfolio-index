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
