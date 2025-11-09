from sqlalchemy.orm import Session

from src.models import User
from src.schemas import UserCreate

class UserService:
    def get_users(self, db: Session) -> list[dict]:
        users = db.query(User).all()
        return [{"id": str(user.id), "name": user.name, "email": user.email } for user in users]
    
    def create_user(self, db: Session, user_data: UserCreate) -> dict:
        db_user = User(name=user_data.name, email=user_data.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return {"id": str(db_user.id), "name": db_user.name, "email": db_user.email}
    
    def get_user(self, db: Session, user_id: str) -> dict | None:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            return {"id": str(user.id), "name": user.name, "email": user.email}
        return None
    
    def update_user(self, db: Session, user_id: str, user_data: UserCreate) -> dict | None:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        for key, value in user_data.model_dump(exclude_unset=True).items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return {"id": str(user.id), "name": user.name, "email": user.email}
    
    def delete_user(self, db: Session, user_id: str) -> bool:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return False
        db.delete(user)
        db.commit()
        return True

    
userService = UserService()