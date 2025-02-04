from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class OwnerModel(BaseModel):
    id: UUID | None = None
    email: str
    password: str
    role: str
    fname: str
    lname: str
    created_at: datetime | None = None
    updated_at: datetime | None = None