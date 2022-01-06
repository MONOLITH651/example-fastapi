from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from pydantic.networks import EmailStr
from pydantic.types import conint

from app.database import Base



class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime


    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Post(PostBase):
    id: int 
    created_at: datetime
    owner_id: int
    owner: UserOut


    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
    # better to specify it as 0, 1
    # conint is lib to make specific integer value
    # conint less or equal to 1
