from fastapi import Depends, FastAPI
from app import users, schemas, database

app = FastAPI()

app.include_router(users.router)


if __name__ == "__main__":
    app()
