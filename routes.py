from fastapi import APIRouter, Depends, Request
from sqlmodel import Session
from db import get_session
from controller.controllerPow import pow_operation
from controller.controllerLog import log_request, get_all_logs
from controller.controllernFib import nFib_operation
from controller.controllerFactorial import factorial_operation
from controller.controllerUser import create_user, get_all_users
from schemas.factorial_schema import FactorialRequest
from schemas.fib_schema import FibRequest
from schemas.pow_schema import PowRequest
from schemas.result_schema import ResultResponse
from schemas.user_create_schema import UserCreateRequest
from utils.response_wraper import api_response


# Main router for all endpoints
router = APIRouter(prefix="/api/v1")


@router.get("/pow", response_model=ResultResponse)
def pow_op(
    req: PowRequest = Depends(),
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
    return api_response({"result": result})


@router.get("/nFib", response_model=ResultResponse)
def nFib_op(
    req: FibRequest = Depends(),
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
    return api_response({"result": result})


@router.get("/factorial", response_model=ResultResponse)
def factorial_op(
    req: FactorialRequest = Depends(),
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
    return api_response({"result": result})


@router.get("/logs/all")
def get_logs(session: Session = Depends(get_session)):
    logs = get_all_logs(session)
    return api_response([log.dict() for log in logs], message="Logs fetched")


@router.post("/user/create")
def create_user_op(
    session: Session = Depends(get_session),
    req: UserCreateRequest = Depends(),
    request: Request = None,
):
    user = create_user(req, session)
    return api_response(
        {"username": user.username, "email": user.email},
        message="User created",
    )


@router.post("/user/login")
def log_in_user(
    session: Session = Depends(get_session),
    req: UserCreateRequest = Depends(),
    request: Request = None,
):
    pass


@router.get("/users")
def get_users(session: Session = Depends(get_session)):
    users = get_all_users(session)
    return api_response(
        [user.model_dump() for user in users], message="users fetched"
    )
