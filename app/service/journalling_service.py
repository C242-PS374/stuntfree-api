import logging
import bcrypt
import base64

from typing import Any
from fastapi import HTTPException

from app.core.config import configs
from app.core import security
from app.repository.nutrition_logs_repository import NutritionLogRepository
from app.service.base_service import BaseService
from app.schema.auth_schema import RegisterSchema, LoginSchema
from app.model.profile import Profile

from app.core.exceptions import DuplicatedError, InternalServerError

class JournallingService(BaseService):
    def __init__(self, nutrition_logs_repository: NutritionLogRepository):
        self.nutrition_logs_repository = nutrition_logs_repository
        
        super().__init__(nutrition_logs_repository) # type: ignore

    def get_today_logs(self, user_id: int) -> Any:
        return self.nutrition_logs_repository.get_today_nutrition_logs(user_id)
    
    def summarize_logs(self) -> Any:
        return self.nutrition_logs_repository.summarize_nutrition_logs()

    def weekly_summarize_logs(self) -> Any:
        return self.nutrition_logs_repository.weekly_summarize_nutrition_logs()