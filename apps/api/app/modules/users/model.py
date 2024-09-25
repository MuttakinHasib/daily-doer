from pydantic import EmailStr
from sqlmodel import Field, SQLModel

from app.common.entity import BaseEntity


class UserBase(SQLModel):
    email: EmailStr = Field(
        unique=True,
        index=True,
    )
    name: str
    avatar: str = Field(nullable=True)
    isSuperUser: bool = False


class UserRegister(SQLModel):
    email: EmailStr
    name: str
    password: str


class UserLogin(SQLModel):
    email: EmailStr
    password: str


class User(BaseEntity, UserBase, table=True):
    password: str = Field(min_length=8)
    pass


class UserPublic(BaseEntity, UserBase):
    pass
