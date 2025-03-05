from app.models.abstract.basemodel import BaseModel
from app.models.hospitalspecialization import HospitalSpecialization
from typing import List
from sqlmodel import Field, Relationship
from uuid import UUID

class Hospital(BaseModel, table=True):
    __tablename__ = "hospitals"
    
    owner_id: UUID = Field(foreign_key="hospitalowners.id", index=True)
    name: str = Field(description="Name of Hospital")
    phone_number: str = Field(description="Phone Number of Hospital")
    email: str = Field(description="Email of Hospital", index=True)
    state: str = Field(description="State of Hospital")
    city: str = Field(description="City of Hospital")
    zipcode: str = Field(description="Zipcode of Hospital")
    street: str = Field(description="Street of Hospital")


    owner: "Owner" = Relationship( #type: ignore
        back_populates="hospitals",
        sa_relationship_kwargs={"lazy": "joined"}
        )
    doctors: List["Doctor"] = Relationship( #type: ignore
        back_populates="hospital"
        )
    
    specialization: List["Specialization"] = Relationship( #type: ignore
        back_populates="hospitals",
        link_model=HospitalSpecialization
    )
    
    patienttohospitalcomments: List["PatientToHospitalComment"] = Relationship(#type: ignore
        back_populates="hospital"
    )

    doctortohospitalcomments: List["DoctorToHospitalComment"] = Relationship( #type: ignore
        back_populates="hospital"
    )