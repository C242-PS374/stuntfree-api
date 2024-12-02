from datetime import datetime
from typing import Any, Union, TypedDict, Optional
from app.repository.user_repository import UserRepository
from app.service.base_service import BaseService
from app.model import Profile
from app.schema import AddPersonalInfo
import grpc
from app.generated import ml_services_pb2, ml_services_pb2_grpc

from fastapi import HTTPException

class MLServiceClient(BaseService):
    def __init__(self, host="localhost", port=52431):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = ml_services_pb2_grpc.MLServiceStub(self.channel)
        
    def predict_nutrition(self, height, weight, age):
        request = ml_services_pb2.NutritionRequest(
            height=height,
            weight=weight,
            age=age
        )
        response = self.stub.PredictNutrition(request)
        return response.nutrition_status

    def predict_stunting(self, age, birth_weight, birth_length, body_weight, body_length, is_sanitized_place, is_healthy_food):
        request = ml_services_pb2.StuntingRequest(
            age=age,
            birth_weight=birth_weight,
            birth_length=birth_length,
            body_weight=body_weight,
            body_length=body_length,
            is_sanitized_place=is_sanitized_place,
            is_healthy_food=is_healthy_food
        )
        response = self.stub.PredictStunting(request)
        return response.stunting_status