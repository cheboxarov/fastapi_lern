from fastapi import FastAPI
import uvicorn
from users.views import router as users_router
from items.views import router as items_router
from contextlib import asynccontextmanager
from core.models.base import Base
from core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(items_router, tags=["Items"])
app.include_router(users_router, tags=["Users"])


@app.get("/")
def hello_index():
    return {"result": "hello world"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)
