from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class HospitalModel(BaseModel):
    id: UUID | None = None
    owner_id: UUID
    name: str
    phone_number: str
    email: str
    state: str
    city: str
    zipcode: str
    street: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

class UpdateHospitalModel(BaseModel):
    owner_id: Optional[UUID] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    zipcode: Optional[str] = None
    street: Optional[str] = None