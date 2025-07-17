from fastapi import APIRouter, Depends, Request
from sqlmodel import Session
from db import get_session
from controller.controllerPow import pow_operation
from controller.controllerLog import log_request
from controller.controllernFib import nFib_operation
from controller.controllerFactorial import factorial_operation
from models.RequestLog import RequestLog
from schemas.factorial_schema import FactorialRequest
from schemas.fib_schema import FibRequest
from schemas.pow_schema import PowRequest
from schemas.result_schema import ResultResponse

router = APIRouter()


@router.post("/pow", response_model=ResultResponse)
def pow_op(
    req: PowRequest,
    session: Session = Depends(get_session),
    request: Request = None,
):
    result = pow_operation(req.base, req.exp)
    log_request(
        operation="pow",
        input_data=f"{req.base},{req.exp}",
        result=str(result),
        session=session,
        request=request,
    )
    return {"result": result}


@router.post("/nFib", response_model=ResultResponse)
def nFib_op(
    req: FibRequest,
    session: Session = Depends(get_session),
    request: Request = None,
):
    result = nFib_operation(req.n)
    log_request(
        operation="nFib",
        input_data=str(req.n),
        result=str(result),
        session=session,
        request=request,
    )
    return {"result": result}


@router.post("/factorial", response_model=ResultResponse)
def factorial_op(
    req: FactorialRequest,
    session: Session = Depends(get_session),
    request: Request = None,
):
    result = factorial_operation(req.n)
    log_request(
        operation="factorial",
        input_data=str(req.n),
        result=str(result),
        session=session,
        request=request,
    )
    return {"result": result}


@router.get("/logs/all")
def get_all_logs(session: Session = Depends(get_session)):
    logs = session.query(RequestLog).all()
    return [log.dict() for log in logs]
