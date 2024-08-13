from fastapi import APIRouter
from .schemas import UserCreate
from . import crud

router = APIRouter(prefix="/users")


@router.post("/")
def create_user(user: UserCreate):
    return crud.create_user(user_in=user)
