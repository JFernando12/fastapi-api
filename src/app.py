from fastapi import FastAPI
from src.routes import project_router, auth_router

def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(project_router, prefix="/api")
    app.include_router(auth_router, prefix="/api")

    return app

app = create_app()