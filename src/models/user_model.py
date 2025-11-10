from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column 

from src.database import Base

class User(Base):
    __tablename__ = "users"

    id = Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name = Mapped[str] = mapped_column(String, nullable=False)
    email = Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)

    auth = relationship("Auth", back_populates="user", uselist=False)
    projects = relationship("Project", back_populates="user")