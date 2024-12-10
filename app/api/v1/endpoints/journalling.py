from dependency_injector.wiring import Provide
from fastapi import APIRouter, Depends, status, UploadFile

from app.core.container import Container
from app.core.middleware import inject
from app.service import MLServiceClient
from app.core.dependencies import get_current_user
from app.service.user_service import UserDict

router = APIRouter(prefix="/journalling", tags=["machine-learning"])

@router.get("/predict/nutrition", status_code=status.HTTP_200_OK)
@inject
def predict_nutrition(
    service: MLServiceClient = Depends(Provide[Container.ml_service]),
    current_user: UserDict = Depends(get_current_user)
):
    user_id = current_user["id"]
    nutrition_status = service.predict_nutrition(user_id)
    return {"nutrition_status": nutrition_status}

@router.post("/food-scan", status_code=status.HTTP_200_OK)
@inject
def predict_image(
    file: UploadFile, 
    current_user: UserDict = Depends(get_current_user),
    service: MLServiceClient = Depends(Provide[Container.ml_service]),
):
    image = file.file.read()
    prediction = service.predict_image(image, current_user["id"])
    return {
        "message": "Food scanning completed",
        "result": prediction
    }