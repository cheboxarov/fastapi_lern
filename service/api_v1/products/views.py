from fastapi import APIRouter

from .schemas import Product, ProductCreate
import crud


router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/")
async def get_products(session):
    return await crud.get_products(session=session)


@router.get("/{product_id}")
async def get_products(product_id: int, session):
    return await crud.get_product(session=session, product_id=product_id)
