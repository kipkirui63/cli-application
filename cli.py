import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Product, Order

# Create a database connection
DATABASE_URL = 'sqlite:///duka.db'
engine = create_engine(DATABASE_URL)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

def add_user(name, email, phone_number):
    # Create a new User record and add it to the session
    new_user = User(user_name=name, user_email=email, user_phone_number=phone_number)
    session.add(new_user)
    session.commit()
    print("User added successfully.")

def delete_user(user_id):
    # Find the User by user_id and delete it
    user = session.query(User).filter_by(user_id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"User with user_id {user_id} deleted successfully.")
    else:
        print(f"User with user_id {user_id} not found.")

def update_user(user_id, new_name, new_email, new_phone_number):
    # Find the User by user_id and update its attributes
    user = session.query(User).filter_by(user_id=user_id).first()
    if user:
        user.user_name = new_name
        user.user_email = new_email
        user.user_phone_number = new_phone_number
        session.commit()
        print(f"User with user_id {user_id} updated successfully.")
    else:
        print(f"User with user_id {user_id} not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manage users in the database")
    parser.add_argument("action", choices=["add", "delete", "update"], help="Action to perform")
    parser.add_argument("--user_id", type=int, help="User ID")
    parser.add_argument("--name", help="User name")
    parser.add_argument("--email", help="User email")
    parser.add_argument("--phone_number", help="User phone number")

    args = parser.parse_args()

    if args.action == "add":
        add_user(args.name, args.email, args.phone_number)
    elif args.action == "delete":
        delete_user(args.user_id)
    elif args.action == "update":
        update_user(args.user_id, args.name, args.email, args.phone_number)
