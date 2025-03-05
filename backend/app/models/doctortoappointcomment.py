from app.models.abstract.basemodel import BaseModel
from app.models.patienttodoctorcomment import Rating
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship

class DoctorToAppointComment(BaseModel, table=True):
    __tablename__ = "doctortoappointcomments"

    appoint_id: UUID = Field(foreign_key="appointments.id", index=True)
    doctor_id: UUID = Field(foreign_key="doctors.id", index=True)
    comment: str = Field(description="Comment is written by doctor to appoint")
    rating: Rating = Field(description="Rating given to comment by Doctor")

    doctor: "Doctor" = Relationship( #type: ignore
        back_populates="doctortoappointcomments",
        sa_relationship_kwargs={"lazy": "joined"}
        )
    
    appoint: "Appointment" = Relationship( #type: ignore
        back_populates="doctortoappointcomments",
        sa_relationship_kwargs={"lazy": "joined"}
    )