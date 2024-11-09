from typing import List, Optional
from pydantic import BaseModel

from app.schema.base_schema import ModelBaseInfo, FindBase, SearchOptions
from app.util.schema import AllOptional

class BaseUser(BaseModel):
    username: str
    email: str
    password: str | None

class User(ModelBaseInfo, BaseUser, metaclass=AllOptional): ...

class FindUser(FindBase, BaseUser, metaclass=AllOptional):
    ...

class FindUserResult(BaseModel):
    data: Optional[List[User]]
    message: str