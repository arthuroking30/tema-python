from pydantic import BaseModel, Field


class PowRequest(BaseModel):
    base: float = Field(..., description="Baza operației de putere")
    exp: int = Field(..., description="Exponentul")


class FibRequest(BaseModel):
    n: int = Field(..., ge=0, description="Numărul de termeni Fibonacci")


class FactorialRequest(BaseModel):
    n: int = Field(..., ge=0, description="Număr pentru factorial")


class ResultResponse(BaseModel):
    result: float | int
