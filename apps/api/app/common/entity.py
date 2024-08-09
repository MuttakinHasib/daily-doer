from datetime import datetime
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class BaseEntity(SQLModel):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
