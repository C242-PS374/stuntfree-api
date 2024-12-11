from typing import Optional
from datetime import datetime
from sqlmodel import Field, Relationship, Enum, Column, DateTime, func

from app.model.base_model import BaseModel

import enum

class Stage(str, enum.Enum):
    pregnancy = "pregnancy"
    infancy = "infancy"

class Gender(str, enum.Enum):
    male = "male"
    female = "female"
    
class Profile(BaseModel, table=True):
    __tablename__: str = "user_profile"

    name: str = Field(nullable=True, default="")
    stage: Optional[Stage] = Field(sa_column=Column(Enum(Stage), nullable=True), default=None)
    child_dob: Optional[str] = Field(nullable=True, default=None)
    child_age: Optional[int] = Field(nullable=True, default=None)
    child_gender: Optional[Gender] = Field(sa_column=Column(Enum(Gender), nullable=True), default=None)
    child_height: Optional[float] = Field(nullable=True, default=None)
    child_weight: Optional[float] = Field(nullable=True, default=None)
    child_born_height: Optional[float] = Field(nullable=True, default=None)
    child_born_weight: Optional[float] = Field(nullable=True, default=None)
    gestasional_age: Optional[int] = Field(nullable=True, default=None)
    address: Optional[str] = Field(nullable=True, default=None)
    is_environment_suitable: Optional[bool] = Field(default=False)
    is_nutrition_fulfilled: Optional[bool] = Field(default=False)
    user_id: int = Field(foreign_key="users.id")

    created_at: Optional[datetime] = Field(sa_column=Column(DateTime(timezone=True), default=func.now()), default=None)
    updated_at: Optional[datetime] = Field(sa_column=Column(DateTime(timezone=True), default=func.now(), onupdate=func.now()), default=None)
    
    user: Optional["User"] = Relationship(back_populates="profile")

from app.model.user import User
User.update_forward_refs()