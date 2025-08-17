from typing import Generic, Optional, TypeVar, DATE
from pydantic import BaseModel
from pydantic import BaseModel, Field
from datetime import date

T = TypeVar("T")

# Shared Characteristics
class Trip(BaseModel):
    country: str
    city: str
    start_date: date
    end_date: date

# Create a Trip
class CreateTrip(Trip):
    pass

# Response Model
class DetailsTrip(Trip):
    user_id: int

    
