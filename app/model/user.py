from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    user_name = Column(String(80), unique=True, index=True, nullable=False)
    email = Column(String(80), unique=True, index=True, nullable=False)
    full_name = Column(String)

    # hashed_password = Column(String)
    # is_active = Column(Boolean, default=True)
