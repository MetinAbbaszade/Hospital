from app.models.abstract.basemodel import BaseModel
from sqlmodel import Field, Relationship
from uuid import UUID
from typing import List



class Patient(BaseModel, table=True):
    __tablename__ = "patients"


    id: UUID = Field(
        foreign_key="users.id",
        primary_key=True,
        unique=True,
        index=True
    )
    fname: str = Field(description="Name of Patient")
    lname: str = Field(description="Surname of Patient")

    user: "User" = Relationship( #type: ignore
        back_populates="patient",
        sa_relationship_kwargs={"lazy": "joined"}
        )
    
    appointments: List["Appointment"] = Relationship( #type: ignore
        back_populates="patient"
        )
    
    patienttodoctorcomments: List["PatientToDoctorComment"] = Relationship( #type: ignore
        back_populates="patient"
    )

    patienttoappointcomments: List["PatientToAppointComment"] = Relationship(#type: ignore
        back_populates="patient"
    )

    patienttohospitalcomments: List["PatientToHospitalComment"] = Relationship(#type: ignore
        back_populates="patient"
    )