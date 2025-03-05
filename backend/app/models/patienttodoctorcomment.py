from app.models.abstract.basemodel import BaseModel
from enum import Enum
from uuid import UUID
from sqlmodel import Field, Relationship


class Rating(str, Enum):
    ONE = "one"
    TWO = "two"
    THREE = "three"
    FOUR = "four"
    FIVE = "five"


class PatientToDoctorComment(BaseModel, table=True):
    __tablename__ = 'patienttodoctorcomments'
    patient_id: UUID = Field(description="Patient id", foreign_key="patients.id", index=True)
    doctor_id: UUID = Field(description="Doctor id", foreign_key='doctors.id', index=True)
    comment: str = Field(description="Comment about doctor")
    rating: Rating = Field(description="Rating of comment")
 
    doctor: "Doctor" = Relationship( #type: ignore
        back_populates="patienttodoctorcomments",
        sa_relationship_kwargs={"lazy": "joined"}
        )
    
    patient: "Patient" = Relationship( #type: ignore
        back_populates="patienttodoctorcomments",
        sa_relationship_kwargs={"lazy": "joined"}
        )
    