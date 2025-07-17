from typing import Any
from fastapi.responses import JSONResponse


def api_response(data: Any, message: str = "Success") -> JSONResponse:
    return JSONResponse(
        content={"status": "ok", "message": message, "data": data}
    )
