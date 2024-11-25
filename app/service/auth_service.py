import logging
import bcrypt

from typing import Any
from passlib.context import CryptContext

from app.core.config import configs
from app.repository.user_repository import UserRepository
from app.service.base_service import BaseService
from app.schema.auth_schema import RegisterSchema
from app.model.profile import Profile

from app.core.exceptions import DuplicatedError, InternalServerError

class AuthService(BaseService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        
        super().__init__(user_repository)

    def sign_up(self, user: RegisterSchema) -> Any:
        is_user_exist = self.user_repository.get_user_by_options("email", user.email)

        if is_user_exist is not None:
            raise DuplicatedError("User with this email already exists")

        encrypted_password = self.hash_password(user.password)
        new_user = self.user_repository.create_user(email=user.email, password=encrypted_password)

        if new_user is None:
            raise InternalServerError("Failed to create user. Please try again later")
        
        user_profile = self.user_repository.create_user_profile(
            Profile(
                name=user.name,
                user_id=new_user.id if new_user.id is not None else 0,
            )
        )
        
        return {
            "message": "User successfully registered",
        }   
        
    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode("utf-8"), salt)

        return hashed.decode("utf-8")
    

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))