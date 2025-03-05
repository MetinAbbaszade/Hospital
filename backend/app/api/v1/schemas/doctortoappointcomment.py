from datetime import datetime
from pydantic import BaseModel
from uuid import UUID
from typing import Optional



class PostDoctorToAppointCommentModel(BaseModel):
    id: UUID | None = None
    appoint_id: UUID
    doctor_id: UUID
    comment: str
    rating: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

class GetDoctorToAppointCommentModel(BaseModel):
    id: UUID
    appoint_id: UUID
    doctor_id: UUID
    comment: str
    rating: str
    created_at: datetime
    updated_at: datetime

class UpdateDoctorToAppointCommentModel(BaseModel):
    id: Optional[UUID] | None = None
    appoint_id: Optional[UUID] | None = None
    doctor_id: Optional[UUID] | None = None
    comment: Optional[str] | None = None
    rating: Optional[str] | None = None
    created_at: Optional[datetime] | None = None
    updated_at: Optional[datetime] | None = None