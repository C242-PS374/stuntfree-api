from dependency_injector.wiring import Provide
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.core.middleware import inject
from app.schema.user_schema import User, FindUser, FindUserResult
from app.service.user_service import UserService

router = APIRouter(prefix="/user", tags=["user"])


@router.get("", response_model=FindUserResult)
@inject
def get_user_list(
    service: UserService = Depends(Provide[Container.user_service]),
):
    return service.get_list(User)