from app.models.doctorspecialization import DoctorSpecialization
from app.persistence.repository import Repository


class DoctorSpecializationRepository(Repository):
    def __init__(self):
        super().__init__(DoctorSpecialization)