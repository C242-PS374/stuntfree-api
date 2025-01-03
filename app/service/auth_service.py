import logging
import bcrypt
import base64

from typing import Any
from fastapi import HTTPException

from app.core.config import configs
from app.core import security
from app.repository.user_repository import UserRepository
from app.service.base_service import BaseService
from app.schema.auth_schema import RegisterSchema, LoginSchema
from app.model.profile import Profile

from app.core.exceptions import DuplicatedError, InternalServerError

class AuthService(BaseService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        
        super().__init__(user_repository) # type: ignore

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
    
    def sign_in(self, credentials: LoginSchema) -> Any:
        result = self.user_repository.get_user_by_options("email", credentials.email)

        if result is None:
            raise HTTPException(status_code=401, detail="Invalid email or password")

        is_password_valid = self.verify_password(credentials.password, result[0].password)

        if not is_password_valid:
            raise HTTPException(status_code=401, detail="Invalid email or password")
        
        access_token = security.create_access_token(
            data={
                "sub": result[0].id
            }
        )

        refresh_token = security.create_refresh_token(
            data={
                "sub": result[0].id
            }
        )

        return {
            "message": "User successfully logged in",
            "token": {
                "token_type": "bearer",
                "access_token": access_token,
                "refresh_token": refresh_token
            },
        }
        
    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode("utf-8"), salt)

        return base64.b64encode(hashed).decode("utf-8")
    

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        hashed_bytes = base64.b64decode(hashed_password)
        return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_bytes)