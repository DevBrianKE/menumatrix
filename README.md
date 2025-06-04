# MenuMatrix CLI Application

## Overview

**MenuMatrix** is a Python-based Command Line Interface (CLI) application designed to manage a restaurant’s menu system. Built using SQLAlchemy for ORM and Alembic for migrations, it offers a smooth, terminal-driven experience to add menu items, place orders, and interact with stored data seamlessly

---

## Learning Goals

- Build a modular CLI application using Python
- Implement SQLAlchemy ORM for persistent data handling
- Apply Alembic for database schema migrations
- Follow clean coding, separation of concerns, and best practices in project organization

---

## Project Structure

```plaintext
.
├── alembic.ini          # Alembic configuration file
├── app.db               # SQLite database file (can be replaced with any DB)
├── CONTRIBUTING.md      # Guidelines for contributing to the project
├── LICENSE.md           # Project license information
├── lib
│   ├── cli.py           # Entry point for the CLI app
│   ├── db.py            # Database engine and session setup
│   ├── helpers.py       # Helper functions for CLI commands
│   ├── debug.py         # Script to manually test models or sessions
│   ├── models
│   │   ├── __init__.py  # Initializes DB connection constants
│   │   └── models.py    # SQLAlchemy models (MenuItem, Order, etc.)
│   └── db
│       ├── session.py   # SQLAlchemy session instance
│       └── app.db       # SQLite database file
├── migrations           # Folder containing Alembic migration scripts
│   ├── versions         # Individual migration scripts
│   └── ...
├── Pipfile              # Defines Python dependencies
├── Pipfile.lock         # Locked Python dependency versions
├── README.md            # Project documentation
```
---

## How to Run the App
### 1. Clone the Repository

```bash
git clone git@github.com:DevBrianKE/menumatrix.git
cd menumatrix
```
### 2.Install dependencies:
```
pipenv install
pipenv shell
```
### 3. Run the database migrations:
```
alembic upgrade head
```
### 4. Start the CLI:
```
python -m lib.cli
```
---

## Features
- View menu items

- Add new menu items

- Place new orders

- View existing orders

- Delete menu items or orders

---

## Tech Stack & Tools

- **Python 3.8+** – Core programming language
- **SQLAlchemy** – ORM for database interactions
- **Alembic** – Database migration tool
- **Tabulate** – For displaying pretty CLI tables
- **SQLite** – Lightweight, file-based relational database
- **Modular Structure** – Scalable and organized codebase

---

## Key Files and Their Roles

### `lib/cli.py`
Main program loop for the CLI:

```
def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()
        if choice == "1":
            # Add a Menu Item
            ...
        elif choice == "2":
            # List Menu Items
            ...
        elif choice == "3":
            # Create New Order
            ...
        elif choice == "4":
            # Add Item to Order
            ...
        elif choice == "5":
            # View Order Items
            ...
        elif choice == "6":
            exit_program()
        else:
            print("Invalid choice, please enter a number between 1 and 6.")

```

## lib/helpers.py

Handles the logic:
```
def view_menu():
    items = session.query(MenuItem).all()
    for item in items:
        print(item)
```
- `add_menu_item(name, price, description=None)`: Adds a new menu item to the database.
- `list_menu_items()`: Retrieves all menu items.
- `create_order()`: Creates a new order.
- `add_item_to_order(order_id, menu_item_id, quantity=1)`: Adds menu items to an existing order.
- `get_order_details(order_id)`: Fetches detailed information about an order.
- `exit_program()`: Gracefully exits the application.


## lib/models/models.py

SQLAlchemy models defining relationships:

```
class MenuItem(Base):
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(250), nullable=True)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    status = Column(String(50), default='pending')
    order_items = relationship('OrderItem', back_populates='order')

class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    menu_item_id = Column(Integer, ForeignKey('menu_items.id'))
    quantity = Column(Integer, default=1)
    order = relationship('Order', back_populates='order_items')
    menu_item = relationship('MenuItem')
```
## lib/db/session.py

Handles session management:
```
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE_URL = "sqlite:///lib/db/app.db"

engine = create_engine(DATABASE_URL, echo=False, future=True)

SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

def get_session():
    return SessionLocal()
```

---

##  Database Migrations with Alembic

### Running Migrations

1. **Modify Models**

Update your models in `lib/models/models.py` as needed.

2. **Generate Migration Script**

```
alembic revision --autogenerate -m "Your migration message"
```
3. Apply the Migration to Your Database

Upgrade your database to reflect the new schema:

```
alembic upgrade head
```
3. Apply Migration

```
alembic upgrade head
```
### Configuration Notes
- Ensure Alembic can detect your models by importing them in your env.py or migration environment:

-In your alembic.ini file, set the database URL:
```
sqlalchemy.url = sqlite:///lib/db/app.db 
```

## Author

**Kipchumba Brian**  
Full-Stack Developer | Software Engineer | Data Enthusiast

- **Portfolio:** [https://devbrianke.github.io/My-Portfolio/](https://devbrianke.github.io/My-Portfolio/)
- **LinkedIn:** [https://www.linkedin.com/in/kipchumba-brian-3a3a41150/](https://www.linkedin.com/in/kipchumba-brian-3a3a41150/)
- **GitHub:** [https://github.com/DevBrianKE](https://github.com/DevBrianKE)
- **Blog:** [My Hashnode Blog](https://devbrianke.hashnode.dev/)

