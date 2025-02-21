from app.models.abstract.basemodel import BaseModel
from sqlmodel import Field, Relationship
from passlib.context import CryptContext
import re
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    DOCTOR = "doctor"
    PATIENT = "patient"
    OWNER = "owner"

context = CryptContext(schemes=["bcrypt"])

class User(BaseModel, table=True):
    __tablename__ = "users"

    role: UserRole = Field(description="Role of User")
    email: str = Field(unique=True, index=True, description="Email of User")
    password: str = Field(description="Password of User")

    patient: "Patient" = Relationship(  # type: ignore
        back_populates="user",
        sa_relationship_kwargs={"lazy": "joined"}
    )

    owner: "Owner" = Relationship(  # type: ignore
        back_populates="user",
        sa_relationship_kwargs={"lazy": "joined"}
    )

    admin: "Admin" = Relationship(  # type: ignore
        back_populates="user",
        sa_relationship_kwargs={"lazy": "joined"}
    )

    doctor: "Doctor" = Relationship(  # type: ignore
        back_populates="user",
        sa_relationship_kwargs={"lazy": "joined"}
    )

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
