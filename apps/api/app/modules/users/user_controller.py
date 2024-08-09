from fastapi import APIRouter, HTTPException
from sqlmodel import col, delete, func, select

from app.core.database import SessionDependency
from app.modules.users.model import User, UserPublic, UserRegister
from app.utils.security import hash_password


router = APIRouter(tags=["Users"], prefix="/users")


@router.get("", response_model=list[UserPublic])
def get_users(session: SessionDependency, skip: int = 0, limit: int = 10):
    count_statement = select(func.count()).select_from(User)
    count = session.exec(count_statement).one()

    statement = select(User).offset(skip).limit(limit)
    users = session.exec(statement).all()

    return [UserPublic.model_validate(user) for user in users]


@router.post("", response_model=UserPublic)
def create_user(session: SessionDependency, body: UserRegister):
    findUserStatement = select(User).where(User.email == body.email)
    existingUser = session.exec(findUserStatement).first()

    if existingUser:
        raise HTTPException(
            status_code=409,
            detail="Looks like you have an account already! Please log in",
        )

    user = User.model_validate(body, update={"password": hash_password(body.password)})
    session.add(user)
    session.commit()
    session.refresh(user)

    return UserPublic.model_validate(user)
