import grpc
import datetime

from fastapi import status
from contextlib import contextmanager
from dateutil.relativedelta import relativedelta

from app.core.config import configs
from app.repository.user_repository import UserRepository
from app.service.base_service import BaseService

from app.generated import ml_services_pb2, ml_services_pb2_grpc

from fastapi import HTTPException

class MLServiceClient(BaseService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        super().__init__(user_repository) # type: ignore

    @contextmanager
    def get_channel_stub(self):
        try:
            with grpc.insecure_channel(f"{configs.GRPC_SERVER_HOST}:{configs.GRPC_SERVER_PORT}") as channel:
                grpc.channel_ready_future(channel).result(timeout=5)
                stub = ml_services_pb2_grpc.MLServiceStub(channel)
                yield stub
        except grpc.RpcError as e:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"Could not connect to gRPC server: {e.details()}", # type: ignore
            )

    def health_check(self):
        with self.get_channel_stub() as stub:
            request = ml_services_pb2.Empty()
            response = stub.HealthCheck(request)
            
            return response.status
        
    def predict_nutrition(self, user_id: int):
        user, profile = self.user_repository.get_user_by_options("id", user_id) or (None, None)
        if user is None or profile is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        if profile.stage != "infancy":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User is not in infancy stage")
        
        height = profile.child_height
        weight = profile.child_weight

        birth_date = profile.child_dob
        age = relativedelta(
            datetime.date.today(),
            datetime.datetime.strptime(str(birth_date), "%Y-%m-%d").date()
        ).years        

        with self.get_channel_stub() as stub:
            request = ml_services_pb2.NutritionRequest(
                height=height,
                weight=weight,
                age=age
            )
            response = stub.PredictNutrition(request)
            return response.nutrition_status

    def predict_stunting(self, age, birth_weight, birth_length, body_weight, body_length, is_sanitized_place, is_healthy_food):
        with self.get_channel_stub() as stub:
            request = ml_services_pb2.StuntingRequest(
                age=age,
                birth_weight=birth_weight,
                birth_length=birth_length,
                body_weight=body_weight,
                body_length=body_length,
                is_sanitized_place=is_sanitized_place,
                is_healthy_food=is_healthy_food
            )
            response = stub.PredictStunting(request)
            return response.stunting_status