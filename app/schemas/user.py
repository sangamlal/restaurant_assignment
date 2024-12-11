from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    role: str  # "customer" or "admin"

class UserResponse(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        orm_mode = True

class LoginRequest(BaseModel):
    username: str
    password: str