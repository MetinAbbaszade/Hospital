from app.persistence.repository import Repository
from app.models.user import User


class UserRepository(Repository):
    def __init__(self):
        super().__init__(User)