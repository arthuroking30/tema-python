from pydantic import BaseModel, Field


class PowRequest(BaseModel):
    base: float = Field(..., description="Baza operației de putere")
    exp: int = Field(..., description="Exponentul")
