from app.models.basemodel import BaseModel
from app.models.user import User
from sqlmodel import Field, Relationship
from uuid import UUID, uuid4
from typing import Optional

class Admin(BaseModel, table=True):
    admin_id : UUID = Field(default_factory=uuid4, primary_key=True, foreign_key='user.id')
    surname: str = Field(description='Surname of Admin')

    user: Optional[User] = Relationship(back_populates='admin')