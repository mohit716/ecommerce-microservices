from pydantic import BaseModel, EmailStr, Field

# Schema for registration input
class UserRegister(BaseModel):
    username: str = Field(..., min_length=3)
    email: EmailStr
    password: str = Field(..., min_length=6)

# Schema for login input
class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)
