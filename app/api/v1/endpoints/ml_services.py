import grpc

from dependency_injector.wiring import Provide
from fastapi import APIRouter, Depends, status
from fastapi import APIRouter, HTTPException, status

from app.core.container import Container
from app.core.middleware import inject
from app.core.config import configs
from app.service import MLServiceClient
from app.core.dependencies import get_current_user
from app.service.user_service import UserService, UserDict

router = APIRouter(prefix="/machine-learning", tags=["machine-learning"])


@router.get("/health-check", status_code=status.HTTP_200_OK)
@inject
def health_check(
    service: MLServiceClient = Depends(Provide[Container.ml_service])
):
    status =  service.health_check()
    return {"status": status}

@router.get("/predict/nutrition", status_code=status.HTTP_200_OK)
@inject
def predict_nutrition(
    service: MLServiceClient = Depends(Provide[Container.ml_service]),
    current_user: UserDict = Depends(get_current_user)
):
    user_id = current_user["id"]
    nutrition_status = service.predict_nutrition(user_id)
    return {"nutrition_status": nutrition_status}

@router.post("/predict/stunting", status_code=status.HTTP_200_OK)
@inject
def predict_stunting():
    pass