from typing import List, Optional
from pydantic import BaseModel, validator

class RegisterSchema(BaseModel):
    email: str
    name: str
    password: str
    confirm_password: str

    @validator("confirm_password")
    def passwords_match(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise ValueError("passwords do not match")
        return v
    
class RegisterResult(BaseModel):
    message: str


class LoginSchema(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    token_type: str
    access_token: str
    refresh_token: str

class LoginResult(BaseModel):
    message: str
    token: Token