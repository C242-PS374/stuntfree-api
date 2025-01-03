from datetime import datetime
from typing import Any, Union, TypedDict, Optional
from app.repository.user_repository import UserRepository
from app.service.base_service import BaseService
from app.model import Profile
from app.schema import AddPersonalInfo

from fastapi import HTTPException

class UserProfileDict(TypedDict):
    id: int
    user_id: int
    stage: str
    name: str
    created_at: datetime | None
    updated_at: datetime | None

class UserDict(TypedDict):
    id: int
    email: str
    password: str | None
    created_at: datetime | None
    updated_at: datetime | None
    profile: UserProfileDict

class UserService(BaseService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        super().__init__(user_repository) # type: ignore

    def get_users(self) -> Any:
        data = self.user_repository.get_users()

        return {
            "data": data,
            "message": "User retrieved successfully"
        }


    def get_user_by_options(self, option: str, value: Union[str, int]) -> UserDict:
        user, profile = self.user_repository.get_user_by_options(option, value) or (None, None)

        if user is None or profile is None:
            raise HTTPException(status_code=404, detail="User not found")
        

        return UserDict(
            id=user.id or 0,
            email=user.email,
            password=user.password,
            created_at=user.created_at,
            updated_at=user.updated_at,
            profile=UserProfileDict(
                id=profile.id or 0, 
                user_id=profile.user_id,
                stage=profile.stage.value if profile.stage else "",
                name=profile.name,
                created_at=profile.created_at,
                updated_at=profile.updated_at
            )
        )
    
    def attach_user_profile(self, user_id: int, profile_info: AddPersonalInfo) -> Profile:
        is_profile_exist = self.user_repository.get_user_by_options("id", user_id)
        if is_profile_exist is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        profile = self.user_repository.update_user_profile(user_id, profile=Profile(**profile_info.model_dump()))

        return profile

        