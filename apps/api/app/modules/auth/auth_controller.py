from fastapi import APIRouter, HTTPException, Response, status
from sqlmodel import select

from app.modules.users.model import User, UserLogin
from app.core.database import SessionDependency
from app.common.model import DefaultMessageResponse
from app.utils.security import verify_password


router = APIRouter(tags=["Auth"], prefix="/auth")


@router.post("/login", response_model=DefaultMessageResponse)
async def login(session: SessionDependency, body: UserLogin, response: Response):
    user = session.exec(select(User).where(User.email == body.email)).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Looks like you don't have an account yet! Please register",
        )
    if not verify_password(body.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Oops! Looks like you entered the wrong password",
        )

    response.set_cookie(key="auth")
    return {"message": "Login successful"}
