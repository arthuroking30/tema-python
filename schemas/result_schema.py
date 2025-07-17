from pydantic import BaseModel


class ResultResponse(BaseModel):
    result: float | int
