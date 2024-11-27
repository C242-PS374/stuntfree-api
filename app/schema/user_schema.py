from typing import List, Optional
from pydantic import BaseModel, Field, validator
from datetime import datetime

from app.schema.base_schema import ModelBaseInfo, FindBase, SearchOptions
from app.util.schema import AllOptional

class Profile(BaseModel):
    id: int
    user_id: int
    name: str
    created_at: datetime | None
    updated_at: datetime | None
    
class BaseUser(BaseModel):
    id: int
    email: str
    password: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    profile: Optional[Profile]

class User(ModelBaseInfo, BaseUser, metaclass=AllOptional): ...

class FindUser(FindBase, BaseUser, metaclass=AllOptional):
    ...

class FindUserResult(BaseModel):
    data: Optional[List[User]]
    message: str

class FindUserByOptions(BaseModel):
    option: str
    value: str | int


class FindUserByOptionsResult(BaseModel):
    data: Optional[User]
    message: str