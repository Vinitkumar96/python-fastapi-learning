
from fastapi import FastAPI

app = FastAPI()  

@app.get("/")
def greet():
    return "welcome vinit"


greet()