from app.models.abstract.basemodel import BaseModel
from sqlmodel import Field, Relationship
from uuid import UUID, uuid4

class Admin(BaseModel, table=True):
    __tablename__ = "admins"
    
    id: UUID = Field(
        foreign_key="users.id",
        primary_key=True,
        unique=True,
        index=True
    )
    fname: str = Field(description="Name of Admin")
    lname: str = Field(description="Surname of Admin")
    role: str = Field(description="Role Admin")

    user: "User" = Relationship( #type: ignore
        back_populates="admin",
        sa_relationship_kwargs={"lazy": "joined"}
        )
