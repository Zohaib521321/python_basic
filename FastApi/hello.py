from fastapi import FastAPI,Query,Header,Path,Body,UploadFile,File,Form,HTTPException,BackgroundTasks
import ItemModel
import datetime
import ItemModel.item_model
import os
import shutil  
from pydantic import  ValidationError
import hashlib
import asyncio
# Create an instance of the FastAPI class
app = FastAPI()

# Define a route using a decorator

@app.get("/")
async def read_root():
    return {"message": "Hello, World"}
@app.get("/item/{item_id}")
async def read_item(item_id=int):
    userData={
     "name":"Zohaib",
     "age":20,
     "language":["python","c++","java"]
    }
    user=ItemModel.item_model.UserDetail(**userData)
    data={
        "name":"Test",
        "description":"Hello This is the test description",
        "price":120 ,
        "userdetail":user
    }
    itemdata=ItemModel.item_model.Item(**data)
    return {"ItemId":item_id,"item":itemdata}
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
@app.post("/add_item")
async def read_items(item:ItemModel.item_model.Item):
    return item


@app.post("/addItem/{itemId}")
async def creatUser(itemId:int =Path(...,title="The ID of an Item"),
                    item:ItemModel.item_model.UserDetail=Body(...,title="The item to create")):
    try:
        ItemModel.item_model.UserDetail(**item.model_dump())
    except ValidationError as e:
        error_message="Validation Error:"+str(e)

        # Raise an HTTPException with status code 422 and include all error details in the response
        raise HTTPException(status_code=422, detail={"errors": error_message})


    return {
        "uniqueId":str(datetime.datetime.now().microsecond),
        "itemId":itemId,
        "name":hashlib.sha256(item.name.encode()).hexdigest(),
        "age":item.age,
        "language":item.language
    }

@app.post("/uploadFile")
async def uploadFileTodisk(file:UploadFile=File(...,title="File"),description:str= Form(...)):
    directory = "/Users/techloset/Documents"
    os.makedirs(directory,exist_ok=True)
    with open(os.path.join(directory,file.filename),"wb") as buffer:
         shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "description": description}
counter=0
async def background_task():
    global counter
    while True:
        await asyncio.sleep(10)
        counter +=1
        print(f"background task number {counter}")
    
@app.get ("/background_task") 
async def start_background_task(background_tasks: BackgroundTasks):
    background_tasks.add_task(background_task)
    return {"message": "Background task started."}




