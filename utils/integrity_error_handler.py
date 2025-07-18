from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError


def integrity_error_handler(request: Request, exc: IntegrityError):
    return JSONResponse(
        status_code=409,
        content={
            "data": None,
            "message": str(exc.orig) if hasattr(exc, "orig") else str(exc),
            "status": "fail",
        },
    )
