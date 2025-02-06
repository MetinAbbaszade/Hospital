from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class PostAdminModel(BaseModel):
    id: UUID | None = None
    email: str
    password: str
    role: str = 'admin'
    lname: str
    fname: str
    created_at: datetime | None = None
    updated_at: datetime | None = None    

class GetAdminModel(BaseModel):
    id: UUID | None = None
    role: str
    lname: str
    fname: str
    created_at: datetime | None = None
    updated_at: datetime | None = None    

class UpdateAdminModel(BaseModel):
    lname: str = None
    fname: str = None