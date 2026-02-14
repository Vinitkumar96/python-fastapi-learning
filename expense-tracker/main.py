from fastapi import FastAPI
from routes.expense import router

app = FastAPI()

app.include_router(router)


@app.get("/")
def home():
    return {"msg": "expense tracker is runinnnnnnngggg"}