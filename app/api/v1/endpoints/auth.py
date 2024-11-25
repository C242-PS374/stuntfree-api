from dependency_injector.wiring import Provide
from fastapi import APIRouter, Depends, status

from app.core.container import Container
from app.core.middleware import inject
from app.schema import RegisterSchema, RegisterResult
from app.service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/signup", status_code=status.HTTP_201_CREATED, response_model=RegisterResult)
@inject
def get_user_by_options(
    user: RegisterSchema,
    service: AuthService = Depends(Provide[Container.auth_service]),
):
    return service.sign_up(user)