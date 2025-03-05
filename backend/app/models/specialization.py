from app.models.abstract.basemodel import BaseModel
from app.models.doctorspecialization import DoctorSpecialization
from app.models.hospitalspecialization import HospitalSpecialization
from sqlmodel import Field, Relationship
from typing import List


class Specialization(BaseModel, table=True):
    __tablename__ = "specializations"
    name: str = Field(description="Name of Specialization")
    description: str = Field(description="Description of Specialization")


    doctors: List["Doctor"] = Relationship( #type: ignore
        back_populates="specialization",
        link_model=DoctorSpecialization
    )

    hospitals: List["Hospital"] = Relationship( #type: ignore
        back_populates="specialization",
        link_model=HospitalSpecialization
    )