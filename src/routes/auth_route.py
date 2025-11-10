from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.database import get_db
from src.services import auth_service
from src.schemas import LoginRequest, RegisterRequest
from src.utils import success_response

auth_router = APIRouter(tags=["auth"], prefix="/auth")

@auth_router.post("/register", status_code=201)
def register(user_data: RegisterRequest, db: Session = Depends(get_db)):
    user = auth_service.register(db, user_data)
    
    if not user:
        raise HTTPException(status_code=400, detail="Registration failed")

    return JSONResponse(
        status_code=201,
        content=success_response(user, 'User registered successfully')
    )

@auth_router.post("/login", status_code=200)
def login(LoginRequest: LoginRequest, db: Session = Depends(get_db)):
    token = auth_service.login(db, LoginRequest)
    
    return JSONResponse(
        status_code=200,
        content=success_response(token, 'Login successful')
    )
