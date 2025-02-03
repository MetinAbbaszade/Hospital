from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class PatientModel(BaseModel):
    id: UUID | None = None
    fname: str
    lname: str
    email: str
    password: str
    role: str | None = 'patient'
    created_at: datetime | None = None
    updated_at: datetime | None = None