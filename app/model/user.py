from typing import Optional
from sqlmodel import Field, Relationship, Date
import enum

from app.model.base_model import BaseModel
from sqlalchemy import Column, Enum
from app.model.profile import Profile


class User(BaseModel, table=True):
    __tablename__: str = "users"

    email: str = Field(index=True, unique=True)
    password: str = Field()
    profile: Optional["Profile"] = Relationship(back_populates="user")
