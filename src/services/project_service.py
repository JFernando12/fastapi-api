from sqlalchemy.orm import Session

from src.models import Project
from src.schemas import ProjectCreate, ProjectUpdate

class ProjectService:
    def get_projects(self, db: Session, user_id: str) -> list[dict]:
        projects = db.query(Project).filter(Project.user_id == user_id).all()
        return [{"id": str(project.id), "name": project.name, "description": project.description} for project in projects]
    
    def create_project(self, db: Session, user_id: str, project_data: ProjectCreate) -> dict:
        db_project = Project(
            name=project_data.name,
            description=project_data.description,
            user_id=user_id
        )

        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        
        return {"id": str(db_project.id), "name": db_project.name, "description": db_project.description}
    
    def get_project(self, db: Session, user_id: str, project_id: str) -> dict | None:
        project = db.query(Project).filter(Project.id == project_id, Project.user_id == user_id).first()
        if not project:
            return None
        return {"id": str(project.id), "name": project.name, "description": project.description}
    
    def update_project(self, db: Session, user_id: str, project_id: str, project_data: ProjectUpdate) -> dict | None:
        project = db.query(Project).filter(Project.id == project_id, Project.user_id == user_id).first()
        if not project:
            return None
        project.name = project_data.name
        project.description = project_data.description
        db.commit()
        db.refresh(project)
        return {"id": str(project.id), "name": project.name, "description": project.description}
    
    def delete_project(self, db: Session, user_id: str, project_id: str) -> bool:
        project = db.query(Project).filter(Project.id == project_id, Project.user_id == user_id).first()
        if not project:
            return False
        db.delete(project)
        db.commit()
        return True
    
project_service = ProjectService()