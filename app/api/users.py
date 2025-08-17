from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.schemas.user import Register, Login, ResponseSchema, TokenResponse
from app.models.user import User
from app.db.database import get_db
from app.services.repo import UsersRepo, BaseRepo
from app.core.security import hash_password, verify_password
from app.core.jwt import JWTRepo
import bcrypt


router = APIRouter(
    tags = {"Authentication"}
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
bcrypt.__about__ = bcrypt

# Register
@router.post("/signup")
async def signup(request: Register, db: Session = Depends(get_db)):
    try:
        _user = User (
            # Insert Data
            username = request.username,
            hashed_password = hash_password(request.password),
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

        if not pwd_context.verify(request.password, _user.hashed_password):
            return ResponseSchema(code="400", status="Bad Request", message="Invalid Password").dict(exclude_none = True)
        
        token = JWTRepo.generate_token({'sub': _user.id})
        return ResponseSchema(
            code="200",
            status="Ok",
            message="Login Success",
            result=TokenResponse(access_token=token, token_type="bearer").dict(exclude_none=True)
        )
    
    except Exception as error:
        error_message = str(error.args)
        print(error_message)
        return ResponseSchema(code="500", status="Error", message="Internal Server Error").dict(exclude_none = True)





