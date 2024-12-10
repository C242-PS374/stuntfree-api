from contextlib import AbstractContextManager
from typing import Callable

from sqlmodel import Session

from app.model import FoodIntake
from app.repository.base_repository import BaseRepository


class FoodRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        super().__init__(session_factory, FoodIntake)

    def create_intake(self, name: str,  user_id: int, qty: int = 1) -> FoodIntake:
        with self.session_factory() as session:
            data = FoodIntake(
                name=name,
                qty=qty,
                user_id=user_id,
                created_at=None,
            )

            session.add(data)
            session.commit()
            session.refresh(data)

            session.expunge_all()
            return data