from app.models.basemodel import UserRole
from app.models.patient import Patient
from app.models.owner import HospitalOwner
from app.models.admin import Admin
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from passlib.context import CryptContext
from uuid import UUID, uuid4
import re

context = CryptContext(schemes=["bcrypt"])

class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    role: UserRole = Field(description="Role of User")
    email: str = Field(unique=True, index=True, description="Email of User")
    password: str = Field(description="Password of User")

    patient: Optional["Patient"] = Relationship(back_populates="user")  
    owner: Optional["HospitalOwner"] = Relationship(back_populates="user")
    admin: Optional["Admin"] = Relationship(back_populates="user")

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
