from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from . config import postgres_host, postgres_name, postgres_password, postgres_username

SQLALCHEMY_DATABASE_URL = f"postgresql://{postgres_username}:{postgres_password}@{postgres_host}/{postgres_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()

    try:
        print("Started Database Connection")
        yield db
    finally:
        print("Closed Database Connection")
        db.close()