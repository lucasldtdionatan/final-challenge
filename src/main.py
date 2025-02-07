from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlmodel import SQLModel

from .database import engine
from src.users.models import *
from src.orders.models import *
from src.catalogs.models import *

from src.catalogs.views import router as catalog_router
from src.users.views import router as user_router
from src.orders.views import router as order_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    # SQLModel.metadata.drop_all(engine)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(catalog_router)
app.include_router(user_router)
app.include_router(order_router)


@app.exception_handler(HTTPException)
async def api_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
        headers=exc.headers,
    )