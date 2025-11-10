import os

class Environment:
    def __init__(self):
        self.DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/fastapi_db")
        self.JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

env = Environment()