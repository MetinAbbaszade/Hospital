from app.models.appointment import AppointmentStatus
from datetime import datetime
from pydantic import BaseModel
from uuid import UUID


class PostAppointmentModel(BaseModel):
    id: UUID | None = None
    patient_id: UUID
    doctor_id: UUID
    date_time: datetime
    problem: str
    status: AppointmentStatus | None = "pending"
    comment: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

class GetAppointmentModel(BaseModel):
    id: UUID
    patient_id: UUID
    doctor_id: UUID
    date_time: datetime
    problem: str
    status: AppointmentStatus | None = "pending"
    comment: str
    created_at: datetime
    updated_at: datetime

class UpdateAppointmentModel(BaseModel):
    patient_id: UUID | None = None
    doctor_id: UUID | None = None
    date_time: datetime | None = None
    problem: str | None =  None
    status: AppointmentStatus | None = None
    comment: str | None = None