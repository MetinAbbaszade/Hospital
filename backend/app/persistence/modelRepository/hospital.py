from app.persistence.repository import Repository
from app.models.hospital import Hospital

class HospitalRepository(Repository):
    def __init__(self):
        super().__init__(Hospital)