from beanie import Document, Link
from typing import Optional, List

from models.event import Event
from pydantic import BaseModel, EmailStr

class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]]

    class Settings:
        name = "user"

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@learn.com",
                "password": "strong!!!",
                "events": [],
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