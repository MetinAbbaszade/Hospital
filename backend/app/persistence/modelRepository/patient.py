from app.persistence.repository import Repository
from app.models.patient import Patient

class PatientRepository(Repository):
    def __init__(self):
        super().__init__(Patient)