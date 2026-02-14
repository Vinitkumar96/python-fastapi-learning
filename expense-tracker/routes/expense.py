from bson import ObjectId
from fastapi import APIRouter, HTTPException, Query
from helpers.serial import serial

from database import expense_collection
from models.expense_model import ExpenseModel
from schemas.expense_scehma import ExpenseSend, ExpenseCreate, ExpenseUpdate

router = APIRouter(prefix="/expense")


@router.post("/", response_model=ExpenseSend)
async def create_expense(expense: ExpenseCreate):
    expense_model = ExpenseModel(
        title = expense.title,
        amount = expense.amount,
        type = expense.type,
        category =expense.categroy,
        record_date =expense.date,
    )

    result = await expense_collection.insert_one(expense_model.to_dict())
    r = await expense_collection.find_one({"_id": result.inserted_id})

    return serial(r)


@router.get("/", response_model=list[ExpenseSend])
async def get_all():
    records = await expense_collection.find().to_list(200)
    return [serial(r) for r in records]


@router.delete("/{id}")
async def delete(id: str):
    result = await expense_collection.delete_one({"_id": ObjectId(id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="not such expense found sirrr")

    return {"message": "delete was a  success"}



@router.get("/filter/",response_model=list[ExpenseSend])
async def fltr(type:str = Query(None), category:str = Query(None)):
    query = {}
    if type:
        query["type"] = type
    if category:
        query["category"] = category

    data = await expense_collection.find(query).to_list(200)
    return [serial(r) for r in data]


@router.get("/summary/all")
async def summary():

    expenses = await expense_collection.find({}).to_list(500)

    income_total = expense_total = 0



    for e in expenses:
        if e["type"] == "income":
            income_total += e["amount"]
        elif e["type"] == "expense":
            expense_total += e["amount"]
    return {
        "total_income": income_total,
        "total_expenses": expense_total,
        "remaining_balance": income_total - expense_total
    }
