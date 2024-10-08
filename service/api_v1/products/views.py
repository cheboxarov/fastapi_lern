from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import Product, ProductCreate
import crud
from core.models import db_helper

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", response_model=list[Product])
async def get_products(session: AsyncSession = Depends(db_helper.session_dependency())):
    return await crud.get_products(session=session)


@router.post("/", response_model=Product)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.session_dependency()),
):
    return await crud.create_product(session=session, product_in=product_in)


@router.get("/{product_id}/", response_model=Product)
async def get_products(
    product_id: int, session: AsyncSession = Depends(db_helper.session_dependency())
):
    product = await crud.get_product(session=session, product_id=product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return await crud.get_product(session=session, product_id=product_id)
