from dependency_injector.wiring import Provide
from typing import List, Any, Dict
from fastapi import APIRouter, Depends, status, UploadFile, Form, File, Body, HTTPException

from app.core.container import Container
from app.core.middleware import inject
from app.service import MLServiceClient, JournallingService
from app.core.dependencies import get_current_user
from app.service.user_service import UserDict

from app.schema.food_schema import FoodSchema

router = APIRouter(prefix="/journalling", tags=["machine-learning"])

@router.post("/food/scan", status_code=status.HTTP_200_OK)
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

@router.get("/food/today", status_code=status.HTTP_201_CREATED)
@inject
def add_food(
    current_user: UserDict = Depends(get_current_user),
    service: JournallingService = Depends(Provide[Container.journalling_service]),
):
    user_id = current_user["id"]

    results = service.get_today_logs(user_id)
    return {
        "message": "Food added",
        "result": results
    }

@router.post("/food/submit-log", status_code=status.HTTP_201_CREATED)
@inject
def submit_food_log(
    current_user: UserDict = Depends(get_current_user),
    service: MLServiceClient = Depends(Provide[Container.ml_service]),
    foods: List[FoodSchema] = Body(...),
    file: UploadFile = File(...),
):
    user_id = current_user["id"]
    
    image = file.file.read() if file else None
    service.predict_nutrition_and_insert(user_id, foods, image)

    return {"message": "Food log submitted"}