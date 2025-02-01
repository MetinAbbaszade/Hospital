from app.models.basemodel import BaseModel
from sqlmodel import Field, Relationship
from uuid import UUID, uuid4
from typing import Optional

class Doctor(BaseModel, table=True):
    doctor_id: UUID = Field(primary_key=True, foreign_key="user.id", default_factory=uuid4)
    hospital_id: UUID = Field(foreign_key="hospital.id", default_factory=uuid4)  # Fixed FK reference
    surname: str = Field(description="Surname of Doctor")
    specialization: str = Field(description="Specialization of Doctor")
    phone_num: str = Field(description="Phone Number of Doctor")
    experience: int = Field(description="Experience of Doctor")

    user: Optional["User"] = None  # Temporary None
    hospital: Optional["Hospital"] = None  # Temporary None

from app.models.user import User
from app.models.hospital import Hospital

Doctor.user = Relationship(back_populates="doctor")
Doctor.hospital = Relationship(back_populates="doctors")
