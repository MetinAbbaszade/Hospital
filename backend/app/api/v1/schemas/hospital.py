from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class HospitalModel(BaseModel):
    id: UUID | None = None
    owner_id: str
    name: str
    phone_number: str
    email: str
    state: str
    city: str
    zipcode: str
    street: str
    created_at: datetime | None = None
    updated_at: datetime | None = None