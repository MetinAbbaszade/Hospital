from datetime import datetime
from pydantic import BaseModel
from uuid import UUID

class GetSpecialization(BaseModel):
    id: UUID
    name: str
    description: str
    created_at: datetime
    updated_at: datetime

class PostSpecialization(BaseModel):
    id: UUID | None = None
    name: str 
    description: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

class UpdateSpecialization(BaseModel):
    name: str | None = None 
    description: str | None = None
