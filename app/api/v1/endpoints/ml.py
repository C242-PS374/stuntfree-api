from dependency_injector.wiring import Provide
from fastapi import APIRouter, Depends, status, UploadFile

from app.core.container import Container
from app.core.middleware import inject
from app.service import MLServiceClient
from app.core.dependencies import get_current_user
from app.service.user_service import UserDict

router = APIRouter(prefix="/machine-learning", tags=["machine-learning"])


@router.get("/health-check", status_code=status.HTTP_200_OK)
@inject
def health_check(
    service: MLServiceClient = Depends(Provide[Container.ml_service])
):
    status =  service.health_check()
    return {"status": status}

@router.post("/predict/stunting", status_code=status.HTTP_200_OK)
@inject
def predict_stunting():
    pass