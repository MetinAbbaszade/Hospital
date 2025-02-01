from app.models.basemodel import BaseModel
from sqlmodel import Field, Relationship
from uuid import UUID, uuid4
from typing import Optional

class HospitalOwner(BaseModel, table=True):
    owner_id: UUID = Field(default_factory=uuid4, primary_key=True, foreign_key="user.id")
    surname: str = Field(description="Surname of Hospital Owner")

    user: Optional["User"] = None 

from app.models.user import User  

HospitalOwner.user = Relationship(back_populates="owner")