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
