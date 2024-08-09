from typing import Annotated
from fastapi import Path, APIRouter

router = APIRouter(prefix="/items")

items = ["asdasd", "gfsdgdfg", "gffgfg"]


@router.get("/latest")
def get_latest_item():
    return {"result": items[-1]}


@router.get("/")
def get_items():
    return {"result": items}


@router.get("/{item_id}")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1000000)]):
    print(item_id)
    return {"result": items[item_id]}
