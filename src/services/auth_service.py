from sqlalchemy.orm import Session

from src.schemas import UserCreate
from src.models import User, Auth
from src.utils import hash_password, verify_password, create_access_token

class AuthService:
    def register(self, db: Session, user_data: UserCreate) -> User:
        hashed_password = hash_password(user_data.password)
        db_user = User(name=user_data.name, email=user_data.email)
        db_auth = Auth(password_hash=hashed_password, user=db_user)
        db.add(db_user)
        db.add(db_auth)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    def login(self, db: Session, email: str, password: str) -> str | None:
        auth = db.query(Auth).join(User).filter(User.email == email).first()
        if not auth or not verify_password(password, auth.password_hash):
            return None
        access_token = create_access_token(data={"sub": str(auth.user_id)})
        return access_token

auth_service = AuthService()