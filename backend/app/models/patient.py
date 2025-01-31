from app.models.basemodel import BaseModel
from app.models.user import User
from sqlmodel import Field, Relationship
from uuid import UUID, uuid4
from typing import Optional

class Patient(BaseModel, table=True):
    patient_id: UUID = Field(default_factory=uuid4, primary_key=True, foreign_key="user.id")
    surname: str = Field(description="Surname of Patient")

    user: Optional["User"] = Relationship(back_populates="patient")
