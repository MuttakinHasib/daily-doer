from fastapi import APIRouter


router = APIRouter(tags=["Tags"], prefix="/tags")


@router.get("")
async def get_tags():
    return {"message": "Get all tags"}
