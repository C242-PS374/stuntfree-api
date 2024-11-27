from dependency_injector.wiring import Provide
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.core.middleware import inject
from app.core.dependencies import get_current_user
from app.schema.user_schema import User, FindUserByOptions, FindUserResult, FindUserByOptionsResult
from app.service.user_service import UserService, UserDict

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/me", response_model=FindUserByOptionsResult)
@inject
def get_user_by_options(
    req: FindUserByOptions,
    service: UserService = Depends(Provide[Container.user_service]),
    current_user: UserDict = Depends(get_current_user)
):
    user = service.get_user_by_options("id", current_user["id"])
    user["password"] = None

    return {
        "data": user,
        "message": "User retrieved successfully"
    }