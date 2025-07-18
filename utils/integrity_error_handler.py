from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError


def global_error_handler(request: Request, exc):
    if isinstance(exc, IntegrityError):
        status_code = 409
        message = str(exc.orig) if hasattr(exc, "orig") else str(exc)
    elif isinstance(exc, HTTPException):
        status_code = exc.status_code
        message = exc.detail
    else:
        status_code = 500
        message = str(exc)
    return JSONResponse(
        status_code=status_code,
        content={
            "data": None,
            "message": message,
            "status": "fail",
        },
    )
