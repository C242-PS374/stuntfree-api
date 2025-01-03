from contextlib import AbstractContextManager
from typing import Callable, Dict, Union, Optional, Tuple

from sqlmodel import Session, select

from app.model import User, Profile
from app.repository.base_repository import BaseRepository
from app.schema.auth_schema import RegisterSchema


class UserRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        super().__init__(session_factory, User)

    def get_users(self):
        with self.session_factory() as session:
            statement = select(User, Profile).join(Profile, isouter=True)
            result = session.exec(statement).all()
            
            data = [
                {
                    "id": user.id,
                    "email": user.email,
                    "password": user.password,
                    "created_at": user.created_at,
                    "updated_at": user.updated_at,
                    "profile": {
                        "id": profile.id,
                        "user_id": profile.user_id,
                        "name": profile.name,
                        "created_at": profile.created_at,
                        "updated_at": profile.updated_at,
                    }
                }
                for user, profile in result
            ]

            return data
        
    def get_user_by_options(self, option: str, value: Union[str, int]) -> Optional[Tuple[User, Profile]]:
        if option not in ["id", "email"]:
            raise ValueError("Invalid option")

        with self.session_factory() as session:
            statement = select(User, Profile).join(Profile, isouter=True).where(getattr(User, option) == value)
            result = session.exec(statement).one_or_none()

            if result is None:
                return None
            
            user, profile = result

            session.expunge_all()
            return user, profile
        
    def create_user(self, email: str, password: str) -> User:
        with self.session_factory() as session:
            user = User(email=email, password=password, id=None, created_at=None, updated_at=None)

            session.add(user)
            session.commit()
            session.refresh(user)

            session.expunge_all()
            return user
        
    def create_user_profile(self, profile: Profile) -> Profile:
        with self.session_factory() as session:
            session.add(profile)
            session.commit()
            session.refresh(profile)

            session.expunge_all()
            return profile
        
    def update_user_profile(self, user_id: int, profile: Profile) -> Profile:
        with self.session_factory() as session:
            statement = select(Profile).where(Profile.user_id == user_id)
            result = session.exec(statement).one()

            result = result.model_copy(update=profile.model_dump(exclude_unset=True))

            result = session.merge(result)
            session.commit()
            session.refresh(result)

            session.expunge_all()
            return result
