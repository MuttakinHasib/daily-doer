import bcrypt
from pydantic import EmailStr
from sqlmodel import Field, SQLModel

from app.common.entity import BaseEntity


class UserRegister(SQLModel):
    email: EmailStr = Field(
        unique=True,
        index=True,
    )
    name: str
    password: str = Field(min_length=6)


class UserBase(UserRegister):
    isSuperUser: bool = False


class User(BaseEntity, UserBase, table=True):
    @property
    def password(self) -> str:
        raise AttributeError("Password is not readable attribute")

    @password.setter
    def password(self, password: str) -> None:
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        self.password = hashed.decode("utf-8")

    def verify_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))
