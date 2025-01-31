from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
from enum import Enum
import re
from passlib.context import CryptContext

context = CryptContext(schemes=['bcrypt'])

class UserRole(str, Enum):
    ADMIN = "admin"
    DOCTOR = "doctor"
    PATIENT = "patient"

class BaseModel(SQLModel):
    name: str = Field(description="Name of Object")
    role: UserRole = Field(description="Role of Object")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    def update(self, data: dict):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "role": self.role.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    role: UserRole = Field(description="Role of User")
    email: str = Field(unique=True, index=True, description="Email of User")
    password: str = Field(description="Password of User")

    patient: Optional["Patient"] = Relationship(back_populates="user")

    def __init__(self, **kwargs):
        email = kwargs.get("email")
        password = kwargs.get("password")

        if email and not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            raise ValueError("Invalid email format!")

        if password:
            kwargs["password"] = self.hash(password)

        super().__init__(**kwargs)

    @staticmethod
    def hash(password: str) -> str:
        return context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return context.verify(plain_password, hashed_password)

class Patient(SQLModel, table=True):
    patient_id: UUID = Field(default_factory=uuid4, primary_key=True, foreign_key="user.id")
    surname: str = Field(description="Surname of Patient")

    user: Optional[User] = Relationship(back_populates="patient")