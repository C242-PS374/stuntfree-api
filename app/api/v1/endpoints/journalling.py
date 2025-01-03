import json

from dependency_injector.wiring import Provide
from typing import List, Any, Dict
from fastapi import APIRouter, Depends, status, UploadFile, Form, File, Body, HTTPException

from app.core.container import Container
from app.core.middleware import inject
from app.service import MLServiceClient, JournallingService
from app.core.dependencies import get_current_user
from app.service.user_service import UserDict

from app.schema.food_schema import FoodSchema, AddFoodLogSchema

router = APIRouter(prefix="/journalling", tags=["machine-learning"])

@router.post("/food/scan", status_code=status.HTTP_200_OK)
@inject
def predict_image(
    current_user: UserDict = Depends(get_current_user),
    service: MLServiceClient = Depends(Provide[Container.ml_service]),
    file: UploadFile = File(...), 
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
        "message": "Today's food logs retrieved",
        "result": results
    }

@router.post("/food/submit-log", status_code=status.HTTP_201_CREATED)
@inject
def submit_food_log(
    current_user: UserDict = Depends(get_current_user),
    service: MLServiceClient = Depends(Provide[Container.ml_service]),
    body: str = Form(...),
    file: UploadFile = File(...),
):
    user_id = current_user["id"]
    
    image = file.file.read() if file else None
    
    try:
        foods = json.loads(body)
        validated_foods = [FoodSchema(**food) for food in foods]
        
        service.predict_nutrition_and_insert(user_id, validated_foods, image)
        
        return {"message": "Food log submitted"}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=f"Validation error: {e}")
    
@router.get("/your-stunting-risk", status_code=status.HTTP_200_OK)
@inject
def get_stunting_risk(
    current_user: UserDict = Depends(get_current_user),
    service: MLServiceClient = Depends(Provide[Container.ml_service]),
):
    user_id = current_user["id"]
    risk = service.predict_stunting(user_id)
    return {
        "message": "Stunting risk calculated",
        "result": risk
    }

# Triggered by the Cloud Scheduler
@router.post("/nutrition/weekly-summary", status_code=status.HTTP_201_CREATED)
@inject
def get_weekly_summary(
    service: JournallingService = Depends(Provide[Container.journalling_service]),
):
    service.weekly_summarize_logs()
    return {
        "message": "Nutrition logs summarized",
    }

# Triggered by the Cloud Scheduler
@router.post("/nutrition/daily-summary", status_code=status.HTTP_201_CREATED)
@inject
def check_summary(
    service: JournallingService = Depends(Provide[Container.journalling_service]),
):

    service.summarize_logs()
    return {
        "message": "Logs summarized",
    }
