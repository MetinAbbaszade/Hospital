from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class AdminModel(BaseModel):
    id: UUID | None = None
    email: str
    password: str
    role: str
    lname: str
    fname: str
    created_at: datetime | None = None
    updated_at: datetime | None = None    