from sqlmodel import SQLModel


class DefaultMessageResponse(SQLModel):
    message: str
