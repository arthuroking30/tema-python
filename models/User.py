from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str = Field(min_length=3, max_length=25, index=True, unique=True)
    email: str = Field(index=True, unique=True)
    password: str = Field(min_length=8)
