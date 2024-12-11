from typing import List, Optional
from pydantic import BaseModel, validator

class FoodSchema(BaseModel):
    name: str
    qty: int

class AddFoodLogSchema(BaseModel):
    foods: List[FoodSchema]
    