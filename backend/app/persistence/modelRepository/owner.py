from app.persistence.repository import  Repository
from app.models.owner import Owner

class OwnerRepository(Repository):
    def __init__(self):
        super().__init__(Owner)