from typing import Generic, Optional, TypeVar
from pydantic import BaseModel
from pydantic import BaseModel, Field

T = TypeVar("T")

# Login
class Login(BaseModel):
    username: str
    password: str

# Register
class Register(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str

    class Config:
        from_attributes = True  

# Response Model
class ResponseSchema(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T] = None

# Token
class TokenResponse(BaseModel):
    access_token: str
    token_type: str