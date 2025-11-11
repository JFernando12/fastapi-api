from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    project_id: int

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    project_id: int | None = None

class TaskRead(BaseModel):
    id: int
    title: str
    description: str | None = None
    project_id: int