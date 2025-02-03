from app.models.abstract.basemodel import BaseModel
from sqlmodel import Field, Relationship
from uuid import UUID
from typing import List

class Owner(BaseModel, table=True):
    __tablename__ = "hospitalowners"
    id: UUID = Field(
        foreign_key="users.id",
        primary_key=True,
        unique=True,  # This ensures one-to-one relationship
        index=True
    )
    fname: str = Field(description="Surname of Hospital Owner")
    lname: str = Field(description="Name of Hospital Owner")
    role: str = Field(description="Role Hospital Owner")

    user: "User" = Relationship(  # type: ignore
        back_populates="owner",
        sa_relationship_kwargs={"lazy": "joined"}
    )

    hospitals: List["Hospital"] = Relationship(  # type: ignore
        back_populates="owner"
    )
