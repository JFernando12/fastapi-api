from sqlalchemy.orm import Session

from src.models import Task
from src.schemas import TaskCreate, TaskUpdate, TaskRead

class TaskService:
    def get_tasks(self, db: Session, user_id: str, project_id: str) -> list[TaskRead]:
        tasks = db.query(Task).filter(Task.user_id==user_id, Task.project_id==project_id).all()
        return [
            TaskRead(
                id=task.id,
                title=task.title,
                description=task.description,
                project_id=task.project_id
            )
            for task in tasks
        ]
    
    def create_task(self, db: Session, user_id: str, task_data: TaskCreate) -> TaskRead:
        db_task = Task(
            title=task_data.title,
            description=task_data.description,
            project_id=task_data.project_id,
            user_id=user_id
        )

        db.add(db_task)
        db.commit()
        db.refresh(db_task)

        return TaskRead(
            id=db_task.id,
            title=db_task.title,
            description=db_task.description,
            project_id=db_task.project_id
        )
    
    def get_task(self, db: Session, user_id: str, task_id: str) -> TaskRead | None:
        task = db.query(Task).filter(Task.id==task_id, Task.user_id==user_id).first()
        if not task:
            return None
        
        return TaskRead(
            id=task.id,
            title=task.title,
            description=task.description,
            project_id=task.project_id
        )
    
    def update_task(self, db: Session, user_id: str, task_id: str, task_data: TaskUpdate) -> TaskRead | None:
        task = db.query(Task).filter(Task.id==task_id, Task.user_id==user_id).first()
        if not task:
            return None
        
        updated_data = task_data.model_dump(exclude_unset=True)
        for key, value in updated_data.items():
            setattr(task, key, value)

        db.commit()
        db.refresh(task)

        return TaskRead(
            id=task.id,
            title=task.title,
            description=task.description,
            project_id=task.project_id
        )
    
    def delete_task(self, db: Session, user_id: str, task_id: str) -> bool:
        task = db.query(Task).filter(Task.id==task_id, Task.user_id==user_id).first()
        if not task:
            return False
        
        db.delete(task)
        db.commit()

        return True
    
task_service = TaskService()