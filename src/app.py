from fastapi import FastAPI
from src.routes import project_route

def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(project_route, prefix="/api/v1")

    return app

app = create_app()