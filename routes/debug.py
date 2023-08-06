from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/ping",
    summary="Debug ping method"
)
def ping():
    return "pong"
