from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.schemas.trip import CreateTrip, TripResponse
from app.models.trip import Trip
from app.db.database import get_db
from app.services.repo import BaseRepo
from app.core.jwt import JWTRepo

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

router = APIRouter(
    tags = {"Trips"}
)

# Create a Trip
@router.post("/create-trip", response_model=TripResponse)
async def create_trip(request: CreateTrip,  db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):

    payload = JWTRepo.decode_token(token)

    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    user_id = int(payload.get("sub"))
    _trip = Trip(
        # Insert Data
        country = request.country,
        city = request.city,
        start_date = request.start_date,
        end_date = request.end_date,
        user_id = user_id
    )

    BaseRepo.insert(db, _trip)

    return _trip

# Get Trip Details
@router.post("/list-trip", response_model = list[TripResponse])
async def get_trip_details(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    payload = JWTRepo.decode_token(token)

    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = "Invalid token")
    
    user_id = int(payload.get("sub"))

    return db.query(Trip).filter(Trip.user_id == user_id).all()







