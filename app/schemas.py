from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    email: EmailStr = Field(examples=["user@example.com"])
    display_name: str = Field(examples=["Jane Doe"])
    password: str = Field(min_length=8)


class LoginRequest(BaseModel):
    email: EmailStr = Field(examples=["user@example.com"])
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    id: int
    email: str
    display_name: str
    created_at: datetime

    model_config = {"from_attributes": True}
