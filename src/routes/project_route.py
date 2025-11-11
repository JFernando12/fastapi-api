from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.services import project_service
from src.schemas import ProjectCreate, ProjectUpdate
from src.database import get_db
from src.utils import success_response, get_current_user

project_router = APIRouter(tags=["projects"], prefix="/projects")

@project_router.get("/", status_code=200)
def get_projects(user_id: str = Depends(get_current_user), db: Session = Depends(get_db)):
    projects = project_service.get_projects(db, user_id=user_id)
    
    return JSONResponse(
        status_code=200,
        content=success_response(data=projects)
    )

@project_router.get("/{project_id}", status_code=200)
def get_project(project_id: str, user_id: str = Depends(get_current_user), db: Session = Depends(get_db)):
    projects = project_service.get_project(db, user_id=user_id, project_id=project_id)
    
    if projects is None:
        raise HTTPException(status_code=400, detail="Project not found")
    
    return JSONResponse(
        status_code=200,
        content=success_response(data=projects)
    )

@project_router.post("/", status_code=201)
def create_project(project_data: ProjectCreate, user_id: str = Depends(get_current_user), db: Session = Depends(get_db)):
    projects = project_service.create_project(db, user_id=user_id, project_data=project_data)
    
    return JSONResponse(
        status_code=201,
        content=success_response(data=projects, message="Project created successfully")
    )

@project_router.delete("/{project_id}")
def delete_project(project_id: str, user_id: str = Depends(get_current_user), db: Session = Depends(get_db)):
    success = project_service.delete_project(db, user_id=user_id, project_id=project_id)
    
    if not success:
        raise HTTPException(status_code=400, detail=f"Not able to delete the project with id: {project_id}")
    
    return JSONResponse(
        status_code=200,
        content=success_response(message="Project deleted successfully")
    )

@project_router.put("/{project_id}", status_code=200)
def update_project(project_id: str, project_data: ProjectUpdate, user_id: str = Depends(get_current_user), db: Session = Depends(get_db)):
    project = project_service.update_project(db, user_id=user_id, project_id=project_id, project_data=project_data)

    if project is None:
        raise HTTPException(status_code=400, detail=f"Not able to update the project with id: {project_id}")
    
    return JSONResponse(
        status_code=200,
        content=success_response(data=project, message="Project updated successfully")
    )
