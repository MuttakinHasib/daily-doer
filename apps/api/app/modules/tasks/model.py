from typing import Optional
from pydantic import EmailStr
from sqlmodel import Field, SQLModel

from app.common.entity import BaseEntity


class TaskBase(SQLModel):
    title: str
    description: Optional[str] = None
    status: str
    priority: int
    due_date: str


class TaskRegister(TaskBase):
    password: str = Field(min_length=6)


class Task(BaseEntity, TaskBase, table=True):
    password: str = Field(min_length=6)
