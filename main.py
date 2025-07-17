from fastapi import FastAPI
from sqlmodel import SQLModel
from db import engine
import routes
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(routes.router)
