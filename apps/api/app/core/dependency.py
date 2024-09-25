from typing import Annotated
from fastapi import Cookie, Depends, HTTPException, status
from sqlmodel import Session, select

from app.core.database import get_database
from app.utils.jwt_token import decode_token
from app.modules.users.model import User, UserPublic

SessionDependency = Annotated[Session, Depends(get_database)]


async def get_current_user(session: SessionDependency, auth: str = Cookie(None)):
    if not auth:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Ops! You need to login first",
        )

    payload = decode_token(auth)
    email = payload.get("email")

    user = session.exec(select(User).where(User.email == email)).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Looks like you don't have an account yet! Please register",
        )

    return UserPublic.model_validate(user)


CurrentUser = Annotated[UserPublic, Depends(get_current_user)]
