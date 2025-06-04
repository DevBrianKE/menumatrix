from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# Define the path to the SQLite database file
DATABASE_URL = "sqlite:///lib/db/app.db"

# Create the SQLAlchemy engine that manages the connection to the database
engine = create_engine(DATABASE_URL, echo=False, future=True)

# Create a thread-safe session factory using scoped_session
SessionLocal = scoped_session(
    sessionmaker(
        autocommit=False,      # Don't auto-commit transactions
        autoflush=False,       # Don't auto-flush changes to the database
        bind=engine,           # Use the engine created above
        expire_on_commit=False # Keep objects usable after commit
    )
)

# Helper function to get a new session from the session factory
def get_session():
    return SessionLocal()
