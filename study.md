## main.py   → starts app
## routes/
   ##    ------ todos.py → contains todo endpoints
## models.py  → defines data structure
## database.py → stores data


# 🌚 job of database.py file
- ✅ Load MongoDB URL
- ✅ Connect to MongoDB
- ✅ Give access to collections (tables)



# Why two folders: models/ and schemas/?

Because they represent two different things:

- models  ->	Database structure	How data is stored in MongoDB
- schemas ->	API structure	How data is received/sent in requests/responses


- what is passed through the api (validation in schemas)
- what is saved in db pass it to the class written in models and then only save it ...to protect db



## If you declare a parameter with a Pydantic model type, FastAPI automatically takes JSON from the request body and puts it into that parameter.

async def create_record(record: RecordCreate):

means:

✅ "Hey FastAPI, expect JSON body and validate it using RecordCreate schema"