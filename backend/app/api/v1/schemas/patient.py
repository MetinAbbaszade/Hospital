from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class PostPatientModel(BaseModel):
    id: UUID | None = None
    fname: str
    lname: str
    email: str
    password: str
    role: str | None = "patient"
    created_at: datetime | None = None
    updated_at: datetime | None = None

class GetPatientModel(BaseModel):
    id: UUID | None = None
    lname: str
    fname: str
    created_at: datetime | None = None
    updated_at: datetime | None = None    

class UpdatePatientModel(BaseModel):
    lname: str | None = None
    fname: str | None = None