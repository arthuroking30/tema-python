from pydantic import BaseModel, Field


class FactorialRequest(BaseModel):
    n: int = Field(..., ge=0, description="Număr pentru factorial")
