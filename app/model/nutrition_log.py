from typing import Optional, List
from sqlmodel import Field, Relationship, DateTime, Column, func
from datetime import datetime

from app.model.base_model import BaseModel
from sqlalchemy import Column


class NutritionLog(BaseModel, table=True):
    __tablename__: str = "nutrition_logs"

    is_akg_fulfilled: bool = Field(default=False)
    user_id: int = Field(foreign_key="users.id", index=True)
    img_url: Optional[str] = Field(nullable=True, default=None)
    foods: List["NutritionLogFoods"] = Relationship(back_populates="nutrition_log")

    created_at: Optional[datetime] = Field(sa_column=Column(DateTime(timezone=True), default=func.now()))

from app.model.nutrition_log_foods import NutritionLogFoods
NutritionLogFoods.update_forward_refs()