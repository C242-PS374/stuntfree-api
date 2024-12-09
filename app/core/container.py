from dependency_injector import containers, providers

from app.core.config import configs
from app.core.database import Database

from app.repository import UserRepository, FoodRepository
from app.service import UserService, AuthService, MLServiceClient


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.endpoints.user",
            "app.api.v1.endpoints.auth",
            "app.api.v1.endpoints.journalling",
            "app.api.v1.endpoints.ml",
            "app.core.dependencies",
        ]
    )

    db = providers.Singleton(Database, db_url=configs.DB_URI)

    user_repository = providers.Factory(UserRepository, session_factory=db.provided.session)
    food_repository = providers.Factory(FoodRepository, session_factory=db.provided.session)

    user_service = providers.Factory(UserService, user_repository=user_repository)
    auth_service = providers.Factory(AuthService, user_repository=user_repository)
    ml_service = providers.Factory(MLServiceClient, user_repository=user_repository, food_repository=food_repository)