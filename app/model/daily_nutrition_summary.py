from typing import Optional
from sqlmodel import Field, Relationship, DateTime, Column, func
from datetime import datetime

from app.model.base_model import BaseModel
from sqlalchemy import Column


class DailyNutritionSummary(BaseModel, table=True):
    __tablename__: str = "daily_nutrition_summaries"
    
    user_id: int = Field(foreign_key="users.id", index=True)
    akg_fulfilled_count: int = Field(default=0)
    akg_not_fulfilled_count: int = Field(default=0)
    akg_fulfilled_mode: int = Field(default=0)

    created_at: Optional[datetime] = Field(sa_column=Column(DateTime(timezone=True), default=func.now()))
