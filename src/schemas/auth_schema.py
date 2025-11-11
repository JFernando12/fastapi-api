from pydantic import BaseModel, EmailStr
from typing import TypedDict

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

class JWTPayload(TypedDict):
    sub: str
    exp: int