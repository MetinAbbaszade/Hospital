from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

class Hospital(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(description="Name of Hospital")
    phone_number: str = Field(description="Phone Number of Hospital")