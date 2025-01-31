from app.models.user import User
from app.models.basemodel import BaseModel
from sqlmodel import Field, Relationship
from uuid import UUID, uuid4
from typing import Optional

class Patient(BaseModel, table=True):
    patient_id: UUID = Field(foreign_key="user.id", primary_key=True, default_factory=uuid4)
    surname: str = Field(description="Surname of Patient")

    user: Optional[User] = Relationship(back_populates="patient")
