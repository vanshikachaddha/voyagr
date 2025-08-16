from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String
from .base import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable = False)
    email = Column(String, nullable = False, unique=True)
    username = Column(String, nullable = False, unique=True)
    hashed_password = Column(String, nullable=False)