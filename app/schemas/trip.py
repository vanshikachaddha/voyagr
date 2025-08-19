from typing import Generic, Optional, TypeVar, DATE
from pydantic import BaseModel
from pydantic import BaseModel, Field
from datetime import date

T = TypeVar("T")

# Shared Characteristics
class TripBase(BaseModel):
    country: str
    city: str
    start_date: date
    end_date: date

# Create a Trip
class CreateTrip(TripBase):
    pass

# Response Model
class TripResponse(TripBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True  