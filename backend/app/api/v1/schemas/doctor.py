from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class DoctorModel(BaseModel):
    id: UUID | None = None
    email: str
    password: str
    hospital_id: UUID
    fname: str
    lname: str
    role: str | None = "doctor"
    specialization: str
    phone_num: str
    experience: int
    created_at: datetime | None = None
    updated_at: datetime | None = None