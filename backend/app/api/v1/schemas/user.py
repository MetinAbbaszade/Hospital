from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class UserModel(BaseModel):
    id: UUID
    fname: str
    lname: str 
    email: str
    password: str
    role: str
    created_at: datetime
    updated_at: datetime