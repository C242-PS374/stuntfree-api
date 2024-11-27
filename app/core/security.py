import jwt
from datetime import datetime, timedelta

from app.core.config import configs

def create_access_token(data: dict):
    to_encode = data.copy()
    if configs.JWT_ACCESS_TOKEN_EXP:
        expire = datetime.utcnow() + timedelta(days=int(configs.JWT_ACCESS_TOKEN_EXP[:-1]))
    else:
        expire = datetime.utcnow() + timedelta(days=1)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode, configs.JWT_SECRET_KEY, algorithm=configs.JWT_ALGORITHM
    )
    
    return encoded_jwt

def create_refresh_token(data: dict):
    to_encode = data.copy()
    if configs.JWT_REFRESH_TOKEN_EXP:
        expire = datetime.utcnow() + timedelta(days=int(configs.JWT_REFRESH_TOKEN_EXP[:-1]))
    else:
        expire = datetime.utcnow() + timedelta(days=30)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, configs.KEY, algorithm=configs.JWT_ALGORITHM)
    return encoded_jwt