from sqlalchemy.orm import Session

from src.models import Project
from src.schemas import ProjectCreate, ProjectUpdate, ProjectRead

class ProjectService:
    def get_projects(self, db: Session, user_id: str) -> list[ProjectRead]:
        projects = db.query(Project).filter(Project.user_id==user_id).all()
        return [
            ProjectRead(
                id=project.id,
                name=project.name,
                description=project.description,
            )
            for project in projects
        ]
    
    def create_project(self, db: Session, user_id: str, project_data: ProjectCreate) -> ProjectRead:
        db_project = Project(
            name=project_data.name,
            description=project_data.description,
            user_id=user_id
        )

        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        
        return ProjectRead(
            id=db_project.id,
            name=db_project.name,
            description=db_project.description,
        )
    
    def get_project(self, db: Session, user_id: str, project_id: str) -> ProjectRead | None:
        project = db.query(Project).filter(Project.id==project_id, Project.user_id==user_id).first()
        if not project:
            return None
        
        return ProjectRead(
            id=project.id,
            name=project.name,
            description=project.description,
        )
    
    def update_project(self, db: Session, user_id: str, project_id: str, project_data: ProjectUpdate) -> ProjectRead | None:
        project = db.query(Project).filter(Project.id==project_id, Project.user_id==user_id).first()
        if not project:
            return None
        
        updated_data = project_data.model_dump(exclude_unset=True)
        for key, value in updated_data.items():
            setattr(project, key, value)
        
        db.commit()
        db.refresh(project)
        
        return ProjectRead(
            id=project.id,
            name=project.name,
            description=project.description,
        )
    
    def delete_project(self, db: Session, user_id: str, project_id: str) -> bool:
        project = db.query(Project).filter(Project.id==project_id, Project.user_id==user_id).first()
        if not project:
            return False
        
        db.delete(project)
        db.commit()
        
        return True
    
project_service = ProjectService()