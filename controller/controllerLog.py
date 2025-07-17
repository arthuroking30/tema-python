from fastapi import Request
from sqlmodel import Session
from models.RequestLog import RequestLog


def extract_source(request: Request) -> str:
    client_host = (
        request.client.host if request and request.client else "unknown"
    )
    client_port = (
        request.client.port if request and request.client else "unknown"
    )
    return f"{client_host}:{client_port}"


def log_request(
    operation: str,
    input_data: str,
    result: str,
    session: Session,
    request: Request,
):

    session.add(
        RequestLog(
            operation=operation,
            input_data=input_data,
            result=result,
            source=extract_source(request),
        )
    )
    session.commit()
