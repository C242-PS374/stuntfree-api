import grpc
import datetime
import json
import re

from fastapi import status
from contextlib import contextmanager
from dateutil.relativedelta import relativedelta

from app.core.config import configs
from app.repository import UserRepository, FoodRepository 
from app.service.base_service import BaseService

from google.cloud import aiplatform
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompt_values import PromptValue
from langchain_google_vertexai import ChatVertexAI

from app.util.template import EXAMPLE_STRUCTURE_RESPONSE

from app.generated import ml_services_pb2, ml_services_pb2_grpc

from fastapi import HTTPException

GRPC_SERVER_URL = configs.GRPC_SERVER_URL

class MLServiceClient(BaseService):
    def __init__(self, user_repository: UserRepository, food_repository: FoodRepository):
        aiplatform.init()

        self.user_repository = user_repository
        self.food_repository = food_repository
        self.genai_model = ChatVertexAI(model="gemini-1.5-flash")

        super().__init__(user_repository) # type: ignore

    @contextmanager
    def get_channel_stub(self):
        try:
            if configs.ENV == "production" or configs.ENV == "stage":
                with grpc.secure_channel(GRPC_SERVER_URL, grpc.ssl_channel_credentials()) as channel:
                    grpc.channel_ready_future(channel).result(timeout=5)
                    stub = ml_services_pb2_grpc.MLServiceStub(channel)
                    yield stub
            else:
                with grpc.insecure_channel(GRPC_SERVER_URL) as channel:
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
        
    def predict_image(self, image: bytes, user_id: int):
        user, profile = self.user_repository.get_user_by_options("id", user_id) or (None, None)

        if user is None or profile is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        try:
            with self.get_channel_stub() as stub:
                request = ml_services_pb2.ImageRequest(image_data=image)
                response = stub.ImageDetection(request)
                
                foods = response.result.split(",")

                if "unknown" in foods:
                    raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Failed to detect food")

                results = []
                for food in foods:
                    food_insert = self.food_repository.create_intake(
                        user_id=user_id,
                        name=food,
                        qty=1
                    )       

                    nutritions = self.genai_model.invoke(
                        self.get_nutrition_from_foods({food: 1})
                    )
                    
                    cleaned_nutrition = re.sub(r'^```json\s*|\s*```$', '', nutritions.content, flags=re.MULTILINE) # type: ignore
                    cleaned_nutrition = re.sub(r"'", '"', cleaned_nutrition)
                    data = json.loads(cleaned_nutrition.strip())

                    results.append({
                        "id": food_insert.id,
                        "name": food_insert.name,
                        "qty": food_insert.qty,
                        "nutrition": data["foods"][0]["nutrition"]
                    }) 

                return results
            
        except grpc.RpcError as e:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"Service unavailable: {e.details()}", # type: ignore
            )
        
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to scan food: {str(e)}"
            )
        
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
        
    
    def get_nutrition_from_foods(self, foods: dict[str, int]) -> PromptValue:
        template = self._get_nutrition_prompt()
        prompt_value = template.invoke(
            {
                "foodnames": list(map(lambda x: f"{x[0]} dengan {x[1]} porsi.", foods.items())),
                "example": EXAMPLE_STRUCTURE_RESPONSE
            }
        )    

        return prompt_value

    def _get_nutrition_prompt(self) -> ChatPromptTemplate:
        template = ChatPromptTemplate([
            ("system", """
            You will become a nutrition specialist. You will predict nutrition with the list of columns I provide. If you don't have a value that matches the column, just give 0.00 (zero). Make sure your predictions are accurate in the units that I provide in list of column, because you are a professional nutrition specialist. Make sure you also reply in Indonesian
            The return will be JSON structure of object 'title' and contains list of object that contain nutrition details based on columns. PLEASE ONCE AGAIN MAKE SURE THAT YOU FOLLOWED THE STRUCTURE OF GIVEN EXAMPLE
            Example:
            {example}
            I don't need any explanation except a well-formatted json format like in the example. Give the key in foods only the name of the food. Don't give it complete with servings.
            """),
            ("human", "Kali ini saya makan dengan {foodnames}"),
        ])

        return template