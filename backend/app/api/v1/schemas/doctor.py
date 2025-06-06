from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID


class PostDoctorModel(BaseModel):
    id: UUID | None = None
    email: str
    password: str
    hospital_id: UUID
    fname: str
    lname: str
    role: str | None = "doctor"
    specialities: List[str] | None = []
    phone_num: str
    experience: int
    created_at: datetime | None = None
    updated_at: datetime | None = None

class GetDoctorModel(BaseModel):
    id: UUID | None = None
    hospital_id: UUID
    fname: str
    lname: str
    phone_num: str
    experience: int
    created_at: datetime | None = None
    updated_at: datetime | None = None

class UpdateDoctorModel(BaseModel):
    hospital_id: Optional[UUID] = None
    fname: Optional[str] = None
    lname: Optional[str] = None
    phone_num: Optional[str] = None
    experience: Optional[int] = None