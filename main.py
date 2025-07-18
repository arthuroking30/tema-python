from fastapi import FastAPI
from sqlmodel import SQLModel
from db import engine
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from utils.integrity_error_handler import global_error_handler
import routes
from contextlib import asynccontextmanager
from fastapi.openapi.utils import get_openapi


@asynccontextmanager
async def lifespan(app):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)
app.add_exception_handler(IntegrityError, global_error_handler)
app.add_exception_handler(HTTPException, global_error_handler)
app.add_exception_handler(RequestValidationError, global_error_handler)
app.include_router(routes.router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="MaaS - Math As A Service",
        version="1.0.0",
        description="""Math functions with JWT Login and
          request logging with ip 💀""",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.setdefault("security", [{"BearerAuth": []}])
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
