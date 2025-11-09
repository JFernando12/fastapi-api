from fastapi import FastAPI
from src.routes import userRouter

def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(userRouter, prefix="/api/v1")

    return app

app = create_app()