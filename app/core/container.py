from dependency_injector import containers, providers

from app.core.config import configs
from app.core.database import Database

from app.repository import UserRepository
from app.service import UserService, AuthService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.endpoints.user",
            "app.api.v1.endpoints.auth",
        ]
    )

    db = providers.Singleton(Database, db_url=configs.DB_URI)

    user_repository = providers.Factory(UserRepository, session_factory=db.provided.session)

    user_service = providers.Factory(UserService, user_repository=user_repository)
    auth_service = providers.Factory(AuthService, user_repository=user_repository)