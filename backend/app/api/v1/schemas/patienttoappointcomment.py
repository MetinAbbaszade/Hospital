from datetime import datetime
from pydantic import BaseModel
from uuid  import UUID


class GetPatientToAppointCommentModel(BaseModel):
    id: UUID
    patient_id: UUID
    appoint_id: UUID
    comment: str
    rating: str
    created_at: datetime
    updated_at: datetime

class PostPatientToAppointCommentModel(BaseModel):
    id: UUID | None = None
    patient_id: UUID
    appoint_id: UUID
    comment: str
    rating: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

class UpdatePatientToAppointCommentModel(BaseModel):
    id: UUID | None = None
    patient_id: UUID | None = None
    appoint_id: UUID | None = None
    comment: str | None = None
    rating: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None