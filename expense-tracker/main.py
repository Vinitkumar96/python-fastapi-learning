from fastapi import FastAPI

app = FastAPI()

# app.add_api_route()


@app.get("/")
def home():
    return {"msg":"expense tracker is runinnnnnnngggg"}