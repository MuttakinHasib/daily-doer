from typing import Optional
from sqlmodel import SQLModel

from app.common.entity import BaseEntity


class TaskBase(SQLModel):
    title: str
    description: Optional[str] = None
    status: str
    priority: int
    due_date: str


class Task(BaseEntity, TaskBase, table=True):
    pass
