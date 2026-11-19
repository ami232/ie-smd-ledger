"""The connection to the database."""

from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session

from ledger.models import Base

DATABASE_URL = "sqlite:///ledger.db"

engine = create_engine(DATABASE_URL)


@event.listens_for(engine, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    """SQLite checks foreign keys only when asked to, once per connection."""
    dbapi_connection.execute("PRAGMA foreign_keys = ON")


def create_tables() -> None:
    """Creates the tables that don't exist yet. Existing tables are not changed."""
    Base.metadata.create_all(engine)


def get_session() -> Session:
    return Session(engine)
