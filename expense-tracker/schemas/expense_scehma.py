from typing import Optional
from pydantic import BaseModel
from datetime import date


class ExpenseCreate(BaseModel):
    title: str
    amount: float
    type: str
    categroy: str  
    date: date


class ExpenseUpdate(BaseModel):
    title: Optional[str] = None
    amount: Optional[float] = None
    type: Optional[str] = None
    category: Optional[str] = None
    date: Optional[date] = None


class ExpenseSend(BaseModel):
    id: str
    title: str
    amount: float
    type: str
    category: str
    date: date