from app.persistence.repository import Repository
from app.models.appointment import Appointment

class AppointmentRepository(Repository):
    def __init__(self):
        super().__init__(Appointment)