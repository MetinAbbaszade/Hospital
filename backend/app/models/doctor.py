from app.models.abstract.basemodel import BaseModel
from app.models.doctorspecialization import DoctorSpecialization
from sqlmodel import Field, Relationship
from uuid import UUID
from typing import List

class Doctor(BaseModel, table=True):
    __tablename__ = "doctors"
    
    id: UUID = Field(
        foreign_key="users.id", 
        primary_key=True, 
        unique=True,
        index=True
    )
    hospital_id: UUID = Field(
        foreign_key="hospitals.id",
        index=True
    )
    fname: str = Field(description="Name of Doctor")
    lname: str = Field(description="Surname of Doctor")
    phone_num: str = Field(description="Phone Number of Doctor")
    experience: int = Field(description="Experience of Doctor")


    specialization: List["Specialization"] = Relationship( #type: ignore
        back_populates="doctors",
        link_model=DoctorSpecialization)
    
    user: "User" = Relationship( #type: ignore
        back_populates="doctor",
        sa_relationship_kwargs={"lazy": "joined"}
        )
    
    hospital: "Hospital" = Relationship( #type: ignore
        back_populates="doctors",
        sa_relationship_kwargs={"lazy": "joined"}
    )

    appointments: List["Appointment"] = Relationship( #type: ignore
        back_populates="doctor"
        )
    
    patienttodoctorcomments: List["PatientToDoctorComment"] = Relationship( #type: ignore
        back_populates="doctor"
        )

    doctortoappointcomments: List ["DoctorToAppointComment"] = Relationship(#type: ignore
        back_populates="doctor"
    )