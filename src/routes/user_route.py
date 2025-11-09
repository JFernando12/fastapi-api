from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.services import userService
from src.schemas import UserCreate, UserRead
from src.database import get_db

userRouter = APIRouter(tags=["users"], prefix="/users")

@userRouter.get("/", status_code=200, response_model=list[UserRead])
def get_users(db: Session = Depends(get_db)):
    users = userService.get_users(db)
    
    return JSONResponse(
        status_code=200,
        content=users
    )

@userRouter.get("/{user_id}", status_code=200, response_model=UserRead)
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = userService.get_user(db, user_id)
    
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")
    
    return JSONResponse(
        status_code=200,
        content=user
    )

@userRouter.post("/", status_code=201, response_model=UserRead)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    user = userService.create_user(db, user_data=user_data)
    
    return JSONResponse(
        status_code=201,
        content=user
    )

@userRouter.delete("/{user_id}", status_code=200)
def delete_user(user_id: str, db: Session = Depends(get_db)):
    success = userService.delete_user(db, user_id)
    
    if not success:
        raise HTTPException(status_code=400, detail=f"No able to delete user with id: {user_id}")
    
    return JSONResponse(
        status_code=200,
        content="User deleted succesfully"
    )

@userRouter.put("/{user_id}", status_code=200, response_model=UserRead)
def update_user(user_id: str, user_data: UserCreate, db: Session = Depends(get_db)):
    user = userService.update_user(db, user_id=user_id, user_data=user_data)

    if user is None:
        raise HTTPException(status_code=400,detail=f"Not able to update the user with id: {user_id}")
    
    return JSONResponse(
        status_code=200,
        content=user
    )