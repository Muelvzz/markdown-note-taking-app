from .database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text

class Notes(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, nullable=False)
    file_name = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))