# lib/db/session.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE_URL = "sqlite:///lib/db/app.db"

engine = create_engine(DATABASE_URL, echo=False, future=True)

SessionLocal = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
        expire_on_commit=False,
    )
)

def get_session():
    return SessionLocal()
