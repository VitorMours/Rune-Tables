import uuid
from datetime import datetime 
from pydantic import BaseModel
from sqlalchemy import UUID, DateTime, String, Integer, Boolean
from sqlalchemy.sql import func
from ..extensions import db

class User(db.Model):

    __tablename__ = "Users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(String(80)) 
    surname = db.Column(String(120))
    email = db.Column(String, unique=True)
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(DateTime(timezone=True), onupdate=func.now())



    def __repr__(self) -> None:
        pass




class UserSchema(BaseModel):
    pass

