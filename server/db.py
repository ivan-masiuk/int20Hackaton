from databases import Database
from sqlalchemy.ext.declarative import declarative_base

from server.settings import DATABASE_URL

database = Database(DATABASE_URL)

Base = declarative_base()


def get_db():
    """
    A dependency for working with PostgreSQL
    """
    return database
