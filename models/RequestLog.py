from sqlmodel import SQLModel, Field


class RequestLog(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    operation: str
    input_data: str
    result: str
    source: str
