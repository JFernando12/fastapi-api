from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    project_id: Mapped[int] = mapped_column(Integer, ForeignKey("projects.id"))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    project = relationship("Project", back_populates="tasks")
    user = relationship("User", back_populates="tasks")