from app.models.abstract.basemodel import BaseModel
from datetime import datetime
import enum
from sqlmodel import Field, Relationship
from uuid import UUID
from typing import List

class AppointmentStatus(str, enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELED = "canceled"
    COMPLETED = "completed"

class Appointment(BaseModel, table=True):
    __tablename__ = "appointments"
    
    patient_id: UUID = Field(foreign_key="patients.id", index=True)
    doctor_id: UUID = Field(foreign_key="doctors.id", index=True)
    date_time: datetime = Field(description="Datetime of appointment", index=True)
    problem: str = Field(description="Problem of patient")
    status: AppointmentStatus = Field(description="Status of appointment", default=AppointmentStatus.PENDING, index=True)
    comment: str = Field(default="", description="Comment from patient")

    patient: "Patient" = Relationship( #type: ignore
        back_populates="appointments",
        sa_relationship_kwargs={"lazy": "joined"}
    )
    
    doctor: "Doctor" = Relationship( #type: ignore
        back_populates="appointments",
        sa_relationship_kwargs={"lazy": "joined"}
    )

    doctortoappointcomments: List["DoctorToAppointComment"] = Relationship(#type: ignore
        back_populates="appoint"
    )
    
    patienttoappointcomments: List["PatientToAppointComment"] = Relationship(#type: ignore
        back_populates="appoint"
    )