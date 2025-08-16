from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.schemas.user import Register, Login, ResponseSchema, TokenResponse
from app.models.user import User
from app.db.database import get_db
from app.services.repo import UsersRepo, BaseRepo
from app.core.config import hash_password, verify_password
from app.core.jst import JWTRepo

router = APIRouter(
    tags = {"Authentication"}
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Register
@router.post("/signup")
async def signup(request: Register, db: Session = Depends(get_db)):
    try:
        _user = User (
            # Insert Data
            username = request.username,
            password = request.password,
            first_name = request.first_name,
            last_name = request.last_name,
            email = request.email)
        UsersRepo.insert(db, _user)
        return ResponseSchema(code="200", status="Ok", message="Success Saved Data").dict(exclude_none=True)
    except Exception as error:
        print(error.args)
        return ResponseSchema(code="500", status="Error", message="Internal Server Error").dict(exclude_none=True)
        
# Login
@router.post("/login")
async def login(request: Login, db: Session = Depends(get_db)):
    try: 
        _user = UsersRepo.find_username(db, User, request.username)

        if not pwd_context.verify(request.password, _user.password):
            return ResponseSchema(code="400", status="Bad Request", message="Invalid Password").dict(exclude_none = True)
        
        token = JWTRepo.generate_token({'sub': _user.username})
        return ResponseSchema(code="200", status="Ok", message="Success Saved Data", result= TokenResponse(access_token = None, token_type = "bearer").dict(exclude_none = True))

    except Exception as error:
        error_message = str(error.args)
        print(error_message)
        return ResponseSchema(code="500", status="Error", message="Internal Server Error").dict(exclude_none = True)





