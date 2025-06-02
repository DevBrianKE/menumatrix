# MenuMatrix CLI Application

## Overview

**MenuMatrix** is a Python-based Command Line Interface (CLI) application built using SQLAlchemy and Alembic to manage a restaurant's menu system. This application allows users to interact with the menu, place orders, and manage menu items through a simple terminal interface. The project showcases a modular design, persistence through SQLAlchemy, and migration management with Alembic.

---

## Learning Goals

- Implement a modular CLI application in Python
- Utilize SQLAlchemy ORM for data persistence
- Handle database migrations with Alembic
- Follow separation of concerns and code organization best practices

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
└── your_database_name.db # Legacy or renamed database (can be ignored)
```
## 1. How to Run the App
### Install dependencies:
```
pipenv install
pipenv shell
```
## 2. Run the database migrations:
```
alembic upgrade head
```
## 3. Start the CLI:
```
python lib/cli.py
```

## Features
- View menu items

- Add new menu items

- Place new orders

- View existing orders

- Delete menu items or orders

## Key Files and Their Roles
lib/cli.py: Main entry point of the app. Contains the main() loop which displays a menu and routes user input to helper functions.
```
def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            view_menu()
```

lib/helpers.py: Contains all helper functions called from the CLI, such as view_menu(), add_menu_item(), and place_order().
```
def view_menu():
    items = session.query(MenuItem).all()
    for item in items:
        print(item)
```
lib/models/models.py: Defines the database models using SQLAlchemy.

```
class MenuItem(Base):
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    
```
lib/db/session.py: Creates and exposes the SQLAlchemy session for use across your app.

## Database Migrations with Alembic
To make changes to your database models:

1. Modify your models in models.py

2. Generate a new migration:
```
alembic revision --autogenerate -m "Add new field to MenuItem"
```

3. Apply the migration:
```
alembic upgrade head
```
## Author
Kipchumba Brian 

