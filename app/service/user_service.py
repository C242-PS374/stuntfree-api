from app.repository.user_repository import UserRepository
from app.service.base_service import BaseService


class UserService(BaseService):
    def __init__(self, role_repository: UserRepository):
        self.role_repository = role_repository
        super().__init__(role_repository)