from app.models.specialization import Specialization
from app.persistence.repository import Repository


class SpecializationRepository(Repository):
    def __init__(self):
        super().__init__(Specialization)

    