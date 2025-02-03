from datetime import datetime, timezone
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, TIMESTAMP
from pydantic import BaseModel


class BaseModel(SQLModel):
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True,
        unique=True
    )

    created_at: datetime = Field(
        nullable=False,
        default_factory=lambda: datetime.now(timezone.utc),
        sa_type=TIMESTAMP(timezone=True)
    )

    updated_at: datetime = Field(
        nullable=False,
        default_factory=lambda: datetime.now(timezone.utc),
        sa_type=TIMESTAMP(timezone=True),
        sa_column_kwargs={
            "onupdate": lambda: datetime.now(timezone.utc)
        }
    )

    def update(self, schema: BaseModel):
        for key, value in schema.model_dump(
            exclude_none=True
        ).items():
            if hasattr(self, key):
                if key != "password":
                    setattr(self, key, value)
                else:
                    setattr(self, key, self.validate_password(value))
        self.updated_at = datetime.now()
