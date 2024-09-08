from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.event import Event

class User(BaseModel):
    email: EmailStr
    password: str


    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@learn.com",
                "password": "strong!!!",
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str


    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@learn.com",
                "password": "strong!!!",
            }
        }