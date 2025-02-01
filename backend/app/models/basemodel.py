from datetime import datetime
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    DOCTOR = "doctor"
    PATIENT = "patient"
    OWNER = "owner"

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
            "name": self.name,
            "role": self.role.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
