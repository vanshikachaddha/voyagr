from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.schemas.trip import Trip, CreateTrip, DetailsTrip
from app.models.user import User
from app.db.database import get_db
from app.services.repo import UsersRepo, BaseRepo
from app.core.security import hash_password, verify_password
from app.core.jwt import JWTRepo
import bcrypt


router = APIRouter(
    tags = {"Trip Creator"}
)

# Create a Trip
@router.post("/create-trip")
async def create_trip(trip: Trip,  db: Session = Depends(get_db)):
    



