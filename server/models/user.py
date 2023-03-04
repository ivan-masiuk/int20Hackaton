from sqlalchemy import (
    Column,
    Boolean,
    String,
    DateTime,
    Integer,
)
from sqlalchemy.sql import func

from server.db import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    password = Column(String(255), nullable=False)
    email = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=True)
    surname = Column(String, nullable=True)
    is_active = Column(Boolean(), default=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
