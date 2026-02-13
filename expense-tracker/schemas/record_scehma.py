from typing import Optional
from unicodedata import category
from pydantic import BaseModel
from datetime import date


class RecordCreate(BaseModel):
    title: str
    amount: float
    type: str
    categroy:str
    date: date




class RecordUpdate(BaseModel):
    title: Optional[str] = None
    amount: Optional[float] = None
    type: Optional[str] = None
    category: Optional[str] = None
    date: Optional[str] = None


class RecordSend(BaseModel):
    title:str
    amount:float
    type:str
    category:str
    date:date