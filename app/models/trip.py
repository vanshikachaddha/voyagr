from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DATE, ForeignKey
from .base import Base

class Trip(Base):
    __tablename__ = "trips"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable = False)
    country = Column(String, nullable = False)
    city = Column(String, nullable = False)
    start_date = Column(DATE, nullable = False)
    end_date = Column(DATE, nullable = False)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="trip")