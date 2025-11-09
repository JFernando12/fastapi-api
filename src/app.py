from fastapi import FastAPI
from .routes import userRouter
from .database.database import SessionLocal

def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(userRouter, prefix="/api/v1")

    return app

app = create_app()