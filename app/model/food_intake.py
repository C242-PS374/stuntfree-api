from typing import Optional
from sqlmodel import Field, Relationship, DateTime, Column, func
from datetime import datetime

from app.model.base_model import BaseModel
from sqlalchemy import Column


class FoodIntake(BaseModel, table=True):
    __tablename__: str = "food_intakes"

    name: str = Field()
    qty: int = Field()
    
    user_id: int = Field(foreign_key="users.id", index=True)

    created_at: Optional[datetime] = Field(sa_column=Column(DateTime(timezone=True), default=func.now()))
