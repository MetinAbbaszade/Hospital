from app.models.abstract.basemodel import BaseModel
from uuid import UUID
from sqlmodel import Field, Relationship

from app.models.patienttodoctorcomment import Rating

class PatientToAppointComment(BaseModel, table=True):
    __tablename__ = "patienttoappointcomments"

    appoint_id: UUID = Field(foreign_key="appointments.id", index=True)
    patient_id: UUID = Field(foreign_key="patients.id", index=True)
    rating : Rating = Field(description="Rating is given by patient to Appointment")
    comment: str = Field(description="Comment is written by patient to Appointment")

    patient: "Patient" = Relationship( #type: ignore
        back_populates="patienttoappointcomments",
        sa_relationship_kwargs={"lazy": "joined"}
    )
    appoint: "Appointment" = Relationship( #type: ignore
        back_populates="patienttoappointcomments",
        sa_relationship_kwargs={"lazy": "joined"}
    )
