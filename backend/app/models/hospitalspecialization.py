from app.models.abstract.basemodel import BaseModel
from sqlmodel import Field
from uuid import UUID

class HospitalSpecialization(BaseModel, table=True):
    hospital_id: UUID = Field(
        foreign_key="hospitals.id",
        primary_key=True,
        index=True
    )
    specialization_id: UUID = Field(
        foreign_key="specializations.id",
        primary_key=True,
        index=True
    )