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