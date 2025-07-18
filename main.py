from fastapi import FastAPI
from sqlmodel import SQLModel
from db import engine
from sqlalchemy.exc import IntegrityError
from utils.integrity_error_handler import integrity_error_handler
import routes
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)
app.add_exception_handler(IntegrityError, integrity_error_handler)
app.include_router(routes.router)
