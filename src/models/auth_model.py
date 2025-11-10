from sqlalchemy import Integer, ForeignKey, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.database import Base

class Auth(Base):
    __tablename__ = "auth"

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    password_hash: Mapped[str] = mapped_column(Text, nullable=False)
    refresh_token: Mapped[str | None] = mapped_column(Text, nullable=True)

    user = relationship("User", back_populates="auth", uselist=False)