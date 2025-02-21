from app.persistence.repository import Repository
from app.models.admin import Admin

class AdminRepository(Repository):
    def __init__(self):
        super().__init__(Admin)