from enum import Enum, auto

from typing import List, Optional
from pydantic import BaseModel, Field, validator, model_validator
from datetime import datetime, date

from app.schema.base_schema import ModelBaseInfo, FindBase, SearchOptions
from app.model.profile import Gender, Stage
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

class AddPersonalInfo(BaseModel):
    stage: Stage

    child_dob: Optional[date] = None
    child_gender: Optional[Gender] = None 
    child_height: Optional[float] = None
    child_weight: Optional[float] = None

    gestasional_age: Optional[int] = None

    address: str
    is_environment_suitable: bool
    is_nutrition_fulfilled: bool

    @model_validator(mode='after')
    def validate_stage_specific_fields(self):
        if self.stage == Stage.infancy:
            required_infancy_fields = ['child_dob', 'child_gender', 'child_height', 'child_weight']
            for field in required_infancy_fields:
                if getattr(self, field) is None:
                    raise ValueError(f"{field} is required for infancy stage")
        
        elif self.stage == Stage.pregnancy:
            if self.gestasional_age is None:
                raise ValueError("gestasional_age is required for pregnancy stage")
        
        common_required_fields = ['address', 'is_environment_suitable', 'is_nutrition_fulfilled']
        for field in common_required_fields:
            if getattr(self, field) is None:
                raise ValueError(f"{field} is required for all stages")
        
        return self


class PersonalInfo(Profile, AddPersonalInfo): ...

class AddPersonalInfoResult(BaseModel):
    data: PersonalInfo
    message: str