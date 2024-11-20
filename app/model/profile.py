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

    name: str = Field(nullable=True)
    stage: Optional[Stage] = Field(sa_column=Column(Enum(Stage), nullable=True))
    child_dob: Optional[str] = Field(nullable=True)
    child_age: Optional[int] = Field(nullable=True)
    child_gender: Optional[Gender] = Field(sa_column=Column(Enum(Gender), nullable=True))
    child_height: Optional[float] = Field(nullable=True)
    child_weight: Optional[float] = Field(nullable=True)
    trimester: Optional[int] = Field(nullable=True)
    address: Optional[str] = Field(nullable=True)
    is_environment_suitable: Optional[bool] = Field(default=False)
    is_nutrition_fulfilled: Optional[bool] = Field(default=False)
    user_id: int = Field(foreign_key="users.id")

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now()))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now(), onupdate=func.now()))
    
    @property
    def user(self):
        from app.model.user import User
        return Relationship(
            back_populates="profile",
            sa_relationship_kwargs={"uselist": False},
        )

