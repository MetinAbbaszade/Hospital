from app.models.abstract.basemodel import BaseModel
from app.models.patienttodoctorcomment import Rating
from uuid import UUID
from sqlmodel import Field, Relationship


class DoctorToHospitalComment(BaseModel, table=True):
    doctor_id: UUID = Field(foreign_key="doctors.id", index=True)
    hospital_id: UUID = Field(foreign_key="hospitals.id", index=True)
    rating: Rating = Field(description="Rating of comment is given to Hospital By Doctor")
    comment: str = Field(description="Comment is given to Hospital By Doctor")

    doctor: "Doctor" = Relationship( #type: ignore
        back_populates="doctortohospitalcomments",
        sa_relationship_kwargs={"lazy":"joined"}
    )

    hospital: "Hospital" = Relationship( #type: ignore
        back_populates="doctortohospitalcomments",
        sa_relationship_kwargs={"lazy": "joined"}
    )