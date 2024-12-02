from dependency_injector.wiring import Provide
from fastapi import APIRouter, Depends, status

from app.core.container import Container
from app.core.middleware import inject

router = APIRouter(prefix="/machine-learning", tags=["machine-learning"])

@router.post("/predict/nutrition", status_code=status.HTTP_200_OK)
@inject
def predict_nutrition():
    pass

@router.post("/predict/stunting", status_code=status.HTTP_200_OK)
@inject
def predict_stunting():
    pass