from datetime import datetime
from pydantic import BaseModel
from uuid import UUID

class PostHospitalSpecializationModel(BaseModel):
    id: UUID | None = None
    hospital_id: UUID
    specialization_id: UUID
    created_at: datetime | None = None
    updated_at: datetime | None = None

class UpdateHospitalSpecializationModel(BaseModel):
    hospital_id: UUID | None = None
    specialization_id: UUID | None = None

class GetHospitalSpecializationModel(BaseModel):
    id: UUID
    hospital_id: UUID
    specialization_id: UUID
    created_at: datetime
    updated_at: datetime