import uuid
from datetime import datetime 
from pydantic import BaseModel, ConfigDict, Field, EmailStr, SecretStr
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import UUID, DateTime, String, Integer, Boolean
from sqlalchemy.orm import Mapped
from sqlalchemy.sql import func
from ..extensions import db

class User(db.Model):

    __tablename__ = "Users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(String(80), nullable=False) 
    surname = db.Column(String(120), nullable=False)
    email = db.Column(String(100), unique=True, nullable=False)
    password = db.Column(String(50), nullable=False)
    created_at = db.Column(DateTime(timezone=True), default=datetime.now, nullable=False)
    updated_at = db.Column(DateTime(timezone=True), default=datetime.now, onupdate=datetime.now, nullable=False)



    def to_json(self) -> None:
        return {"name":self.name,"surname":self.surname,"email":self.email}


    def __repr__(self) -> None:
        return f"<User: {self.name} {self.surname}: {self.email}>"

class UserSchema(BaseModel):
    name: str 
    surname: str
    email: EmailStr
    password: SecretStr 

    class Config:
        from_attributes = True



