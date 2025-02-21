from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class PostOwnerModel(BaseModel):
    id: UUID | None = None
    email: str
    password: str
    fname: str
    lname: str
    role: str | None = "owner"
    created_at: datetime | None = None
    updated_at: datetime | None = None

class GetOwnerModel(BaseModel):
    id: UUID | None = None
    fname: str
    lname: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

class UpdateOwnerModel(BaseModel):
    fname: Optional[str] = None
    lname: Optional[str] = None