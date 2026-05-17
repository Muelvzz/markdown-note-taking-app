import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")
redis_db = os.getenv("REDIS_DB")
redis_password = os.getenv("REDIS_PASSWORD")
redis_ttl_seconds = os.getenv("REDIS_TTL_SECONDS")

allowed_extensions = (".md", ".markdown")

postgres_username = os.getenv("POSTGRES_USERNAME")
postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_host = os.getenv("POSTGRES_HOST")
postgres_name = os.getenv("POSTGRES_NAME")

origins = [
    "http://localhost:5173",
]

notes_folder = Path(os.path.join("notes"))