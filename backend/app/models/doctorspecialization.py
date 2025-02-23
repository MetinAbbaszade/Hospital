from app.models.abstract.basemodel import BaseModel
from sqlmodel import Field
from uuid import UUID

class DoctorSpecialization(BaseModel, table=True):
    doctor_id: UUID = Field(
        foreign_key="doctors.id",
        primary_key=True,
        index=True
    )
    specialization_id: UUID = Field(
        foreign_key="specializations.id",
        primary_key=True,
        index=True
    )