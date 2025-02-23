from datetime import datetime
from pydantic import BaseModel
from uuid import UUID

class PostDoctorSpecializationModel(BaseModel):
    id: UUID | None = None
    doctor_id: UUID
    specialization_id: UUID
    created_at: datetime | None = None
    updated_at: datetime | None = None

class UpdateDoctorSpecializationModel(BaseModel):
    doctor_id: UUID | None = None
    specialization_id: UUID | None = None

class GetDoctorSpecializationModel(BaseModel):
    id: UUID
    doctor_id: UUID
    specialization_id: UUID
    created_at: datetime
    updated_at: datetime