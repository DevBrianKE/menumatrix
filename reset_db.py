from lib.db import engine, Base  # adjust if needed
from lib.models.models import MenuItem, OrderItem, Order

def reset_database():
    print("Dropping tables if they exist...")
    OrderItem.__table__.drop(engine, checkfirst=True)
    MenuItem.__table__.drop(engine, checkfirst=True)
    Order.__table__.drop(engine, checkfirst=True)

    print("Creating tables...")
    Base.metadata.create_all(engine)

    print("Database reset complete!")

if __name__ == "__main__":
    reset_database()
