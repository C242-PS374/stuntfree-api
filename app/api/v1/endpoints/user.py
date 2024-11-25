from dependency_injector.wiring import Provide
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.core.middleware import inject
from app.schema.user_schema import User, FindUserByOptions, FindUserResult, FindUserByOptionsResult
from app.service.user_service import UserService

router = APIRouter(prefix="/user", tags=["user"])


@router.get("", response_model=FindUserResult)
@inject
def get_user_list(
    service: UserService = Depends(Provide[Container.user_service]),
):
    return service.get_users()

@router.get("/detail", response_model=FindUserByOptionsResult)
@inject
def get_user_by_options(
    req: FindUserByOptions,
    service: UserService = Depends(Provide[Container.user_service]),
):
    return service.get_user_by_options(req.option, req.value)