from app.models.abstract.basemodel import BaseModel
from typing import List
from sqlmodel import Field, Relationship
from uuid import UUID

class Hospital(BaseModel, table=True):
    __tablename__ = "hospitals"
    
    owner_id: UUID = Field(foreign_key="hospitalowners.id", index=True)
    name: str = Field(description="Name of Hospital")
    phone_number: str = Field(description="Phone Number of Hospital")
    email: str = Field(description="Email of Hospital")
    state: str = Field(description="State of Hospital", index=True)
    city: str = Field(description="City of Hospital", index=True)
    zipcode: str = Field(description="Zipcode of Hospital", index=True)
    street: str = Field(description="Street of Hospital", index=True)


    owner: "Owner" = Relationship( #type: ignore
        back_populates="hospitals",
        sa_relationship_kwargs={"lazy": "joined"}
        )
    doctors: List["Doctor"] = Relationship( #type: ignore
        back_populates="hospital"
        )