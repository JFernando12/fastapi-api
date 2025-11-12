from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.services import task_service
from src.schemas import TaskCreate, TaskUpdate
from src.database import get_db
from src.utils import success_response, get_current_user

task_router = APIRouter(tags=["tasks"], prefix="/tasks")

@task_router.get("/{project_id}", status_code=200)
def get_tasks(project_id: int, user_id: str = Depends(get_current_user), db: Session = Depends(get_db)):
    tasks = task_service.get_tasks(db, user_id=user_id, project_id=project_id)

    return JSONResponse(
        status_code=200,
        content=success_response(data=tasks)
    )

@task_router.get("/{task_id}")
def get_tasks(project_id: int, task_id: int, user_id: str = Depends(get_current_user), db: Session = Depends(get_db)):
    task = task_service.get_task(db, user_id=user_id, task_id=task_id)

    if task is None:
        raise HTTPException(status_code=400, detail="Task not found")
    
    return JSONResponse(
        status_code=200,
        content=success_response(data=task)
    )

@task_router.post("/", status_code=201)
def create_task(task_data: TaskCreate, user_id: str = Depends(get_current_user), db: Session = Depends(get_db)):
    task = task_service.create_task(db, user_id=user_id, task_data=task_data)

    return JSONResponse(
        status_code=201,
        content=success_response(data=task, message="Task created successfully")
    )

@task_router.delete("/{task_id}")
def delete_task(task_id: str, user_id: str = Depends(get_current_user), db: Session = Depends(get_db)):
    success = task_service.delete_task(db, user_id=user_id, task_id=task_id)

    if not success:
        raise HTTPException(status_code=400, detail=f"Not able to delete the task with id: {task_id}")
    
    return JSONResponse(
        status_code=200,
        content=success_response(message="Task deleted successfully")
    )

@task_router.put("/{task_id}", status_code=200)
def update_task(task_id: str, task_data: TaskUpdate, user_id: str = Depends(get_current_user), db: Session = Depends(get_db)):
    task = task_service.update_task(db, user_id=user_id, task_id=task_id, task_data=task_data)

    if task is None:
        raise HTTPException(status_code=400, detail=f"Not able to update the task with id: {task_id}")
    
    return JSONResponse(
        status_code=200,
        content=success_response(data=task, message="Task updated successfully")
    )
