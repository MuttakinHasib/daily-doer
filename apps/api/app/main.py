from fastapi import FastAPI

from app.core.config import settings
from app.modules.users import user_controller


app = FastAPI(title="Daily Doer API", version="0.1.0")


@app.get("/", tags=["Root"])
async def root() -> dict:
    print(settings.DATABASE_URL)
    return {"message": "Assalamua Alaikum, Welcome to the Daily Doer API"}


app.include_router(user_controller.router)
