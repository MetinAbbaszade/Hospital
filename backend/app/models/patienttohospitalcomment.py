from app.models.abstract.basemodel import BaseModel
from uuid import UUID
from sqlmodel import Field, Relationship
from app.models.patienttodoctorcomment import Rating

class PatientToHospitalComment(BaseModel, table=True):
    __tablename__ = "patienttohospitalcomments"

    hospital_id: UUID = Field(foreign_key="hospitals.id", index=True)
    patient_id: UUID = Field(foreign_key="patients.id", index=True)
    rating : Rating = Field(description="Rating is given by patient to Appointment")
    comment: str = Field(description="Comment is written by patient to Appointment")

    patient: "Patient" = Relationship( #type: ignore
        back_populates="patienttohospitalcomments",
        sa_relationship_kwargs={"lazy": "joined"}
    )
    hospital: "Hospital" = Relationship( #type: ignore
        back_populates="patienttohospitalcomments",
        sa_relationship_kwargs={"lazy": "joined"}
    )