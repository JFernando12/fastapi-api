from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name = Mapped[str] = mapped_column(String, nullable=False)
    description = Mapped[str | None] = mapped_column(String, nullable=True)