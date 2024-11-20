from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlmodel import Column, DateTime, Field, SQLModel, func

class BaseModel(SQLModel):
    id: int = Field(primary_key=True, index=True)
