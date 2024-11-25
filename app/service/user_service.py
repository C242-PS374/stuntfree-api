from typing import Any
from app.repository.user_repository import UserRepository
from app.service.base_service import BaseService


class UserService(BaseService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        super().__init__(user_repository)

    def get_users(self) -> Any:
        data = self.user_repository.get_users()

        return {
            "data": data,
            "message": "User retrieved successfully"
        }


    def get_user_by_options(self, option: str, value: str | int) -> Any:
        user, profile = self.user_repository.get_user_by_options(option, value) or (None, None)

        if user is None or profile is None:
            return {
                "data": None,
                "message": "User not found"
            }
        

        return {
            "data": {
                "id": user.id,
                "email": user.email,
                "password": user.password,
                "created_at": user.created_at,
                "updated_at": user.updated_at,
                "profile": {
                    "id": profile.id,
                    "user_id": profile.user_id,
                    "name": profile.name,
                    "created_at": profile.created_at,
                    "updated_at": profile.updated_at,
                }
            },
            "message": "User retrieved successfully"
        }