from typing import Callable, List
from contextlib import AbstractContextManager
from datetime import datetime, time, timedelta, date
from collections import Counter

from fastapi import HTTPException

from sqlmodel import Session, select
from sqlalchemy.orm import joinedload

from app.model import NutritionLog, NutritionLogFoods, DailyNutritionSummary
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
            
            statement = select(NutritionLog).where(
                (NutritionLog.created_at or date.today()) >= start_of_today, # or date.today() is only for passing pylance, created_at will never be None
                (NutritionLog.created_at or date.today()) < end_of_today,
                NutritionLog.user_id == user_id, 
            )

            exec = session.exec(statement).one()

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

    def summarize_nutrition_logs(self):
        with self.session_factory() as session:
            try:
                today = date.today()

                statement = select(NutritionLog.user_id, NutritionLog.is_akg_fulfilled).where(
                    (NutritionLog.created_at or date.today()) >= today,
                )

                logs = session.exec(statement).all()
                print(logs)
                user_logs = {}
                for log in logs:
                    user_logs.setdefault(log.user_id, []).append(log.is_akg_fulfilled) # type: ignore

                for user_id, is_akg_fulfilled_list in user_logs.items():
                    
                    count_true = is_akg_fulfilled_list.count(True)
                    count_false = is_akg_fulfilled_list.count(False)

                    mode = Counter(is_akg_fulfilled_list).most_common(1)[0][0]

                    existing_summary = session.exec(
                        select(DailyNutritionSummary).where(
                            DailyNutritionSummary.user_id == user_id,
                            (DailyNutritionSummary.created_at or date.today()) >= today,
                        )
                    ).one_or_none()

                    if existing_summary:
                        existing_summary.akg_fulfilled_count = count_true
                        existing_summary.akg_not_fulfilled_count = count_false
                        existing_summary.akg_fulfilled_mode = mode
                    else:
                        summary = DailyNutritionSummary(
                            user_id=user_id,
                            akg_fulfilled_count=count_true,
                            akg_not_fulfilled_count=count_false,
                            akg_fulfilled_mode=1 if mode else 0,
                            created_at=None
                        )

                        session.add(summary)
                
                session.commit()

                return True

            except Exception as e:
                print(e)
                session.rollback()
                raise HTTPException(status_code=500, detail="Internal Server Error")

