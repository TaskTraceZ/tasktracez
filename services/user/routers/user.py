from fastapi import APIRouter

router = APIRouter()


@router.post(
    "/user/",
    tags=["user"],
)
async def create_user():
    return [{"username": "Rick"}, {"username": "Morty"}]
