from pydantic import BaseModel, EmailStr, Field


class UserCreateRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=25)
    email: EmailStr
    password: str = Field(..., min_length=8)
