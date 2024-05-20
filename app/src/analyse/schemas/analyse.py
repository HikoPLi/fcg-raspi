from typing import Optional, List
from pydantic import BaseModel
# from beanie import Document
from pydantic import BaseModel, Field
from datetime import datetime


class GarbageType(BaseModel):
    recyclable: bool
    hazardous: bool
    food: bool
    other: bool


class Record(BaseModel):
    success: bool
    object: str
    material: str
    isMetal: bool
    type: GarbageType
    detail: str
    time: Optional[datetime] = Field(default_factory=datetime.utcnow)


class Auth(BaseModel):
    userID: str
    record: List[Record]


class AnalyseDocument( Auth):
    class Settings:
        name = "analyse"
        timestamps = True
