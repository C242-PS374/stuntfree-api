from typing import Optional
from sqlmodel import Field, Relationship, DateTime, Column, func
from datetime import datetime

from app.model.base_model import BaseModel
from sqlalchemy import Column


class NutritionLogFoods(BaseModel, table=True):
    __tablename__: str = "nutrition_log_foods"
    
    name: str = Field()
    qty: int = Field()

    nutrition_log_id: int = Field(foreign_key="nutrition_logs.id", index=True)
    nutrition_log: Optional["NutritionLog"] = Relationship(back_populates="foods")
    created_at: Optional[datetime] = Field(sa_column=Column(DateTime(timezone=True), default=func.now()))

from app.model.nutrition_log import NutritionLog
NutritionLog.update_forward_refs()