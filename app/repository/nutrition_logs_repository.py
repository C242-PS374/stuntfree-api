from typing import Callable, List
from contextlib import AbstractContextManager
from datetime import datetime, time, timedelta, date

from fastapi import HTTPException

from sqlmodel import Session, select
from sqlalchemy.orm import joinedload

from app.model import NutritionLog, NutritionLogFoods
from app.schema.food_schema import FoodSchema
from app.repository.base_repository import BaseRepository
from datetime import date


class NutritionLogRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        super().__init__(session_factory, NutritionLog)

    def add_nutrition_logs(self, foods:  List[FoodSchema], img_url: str | None, user_id: int, is_akg_fulfilled: bool = False):
        with self.session_factory() as session:
            try:
                data = NutritionLog(
                    is_akg_fulfilled=is_akg_fulfilled,
                    img_url=img_url,
                    user_id=user_id,
                    created_at=None,
                )

                session.add(data)
                session.commit()
                session.refresh(data)

                for food in foods:
                    session.add(
                        NutritionLogFoods(
                            name=food.name,
                            qty=food.qty,
                            nutrition_log_id=int(data.id or 0),
                            created_at=None
                        )
                    )

                session.commit()
                session.refresh(data)

                session.expunge_all()
                return data
            except Exception as e:
                session.rollback()
    
    def get_today_nutrition_logs(self, user_id: int):
        with self.session_factory() as session:
            today = date.today()
            start_of_today = datetime.combine(today, time())
            end_of_today = start_of_today + timedelta(days=1)

            print(end_of_today)

            statement = select(NutritionLog).where(
                (NutritionLog.created_at or date.today()) >= start_of_today,
                (NutritionLog.created_at or date.today()) < end_of_today,
                NutritionLog.user_id == user_id, 
            )

            exec = session.exec(statement).one_or_none()

            if exec is None:
                return []

            results = {
                "id": exec.id,
                "is_akg_fulfilled": exec.is_akg_fulfilled,
                "user_id": exec.user_id,
                "img_url": exec.img_url,
                "created_at": exec.created_at,
                "foods": [{"id": food.id, "name": food.name, "qty": food.qty} for food in exec.foods],
            }

            session.expunge_all()
            return results

