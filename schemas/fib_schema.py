from pydantic import BaseModel, Field


class FibRequest(BaseModel):
    n: int = Field(..., ge=0, description="Numărul de termeni Fibonacci")
