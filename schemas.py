from typing import Optional
from pydantic import BaseModel, constr
from datetime import datetime

class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=50)
    password: constr(min_length=6)

class UserRead(BaseModel):
    id: int
    username: str
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TaskCreate(BaseModel):
    title: constr(min_length=1)
    description: Optional[str] = None

class TaskUpdate(BaseModel):
    title: Optional[constr(min_length=1)] = None
    description: Optional[str] = None
    is_done: Optional[bool] = None

class TaskRead(BaseModel):
    id: int
    title: str
    description: Optional[str]
    is_done: bool
    owner_id: Optional[int]
    created_at: datetime

    class Config:
        orm_mode = True
