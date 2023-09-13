from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, User, Product, Order  # Assuming your models are defined in "models.py"

# Create a database connection
DATABASE_URL = 'sqlite:///duka.db'

Base = declarative_base()

# Create a database engine
engine = create_engine(DATABASE_URL)

# Create tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Seed data
def seed_data():
    # Seed users
    user1 = User(user_id=1, user_name="stanoo", user_email="stanoo@gmail.com", user_phone_number="0724-613-265")
    user2 = User(user_id=2, user_name="enock", user_email="enock@gmail.com", user_phone_number="0745-613-265")

    # Seed products
    product1 = Product(product_id=22, product_name="tea")
    product2 = Product(product_id=23, product_name="milk")

    # Seed orders
    order1 = Order(order_id="01", user_id=1)

    # Add data to the session
    session.add_all([user1, user2, product1, product2, order1])
    session.commit()

if __name__ == "__main__":
    seed_data()
