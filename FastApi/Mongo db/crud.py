from fastapi import FastAPI,Body,HTTPException
from item_model import AddItem
from constants import AppConstant
import pymongo
from bson import ObjectId
from datetime import datetime
from pymongo.errors import PyMongoError

app=FastAPI()
@app.get("/")
async def defaultMessage():
    return {"Message":"Successfully build connection"}
@app.post("/createItem")
async def createItem(item: AddItem = Body(..., title="Add Item for task")):
    taskCollection = AppConstant.db.get_collection1()
    newItem={
        "_id":AppConstant.uniqueid(),
        "itemName":item.itemName,
        "isCompleted":item.isComleted,
        "priority":item.priority,
        "createdAt":datetime.now()
    }

    try:
         taskCollection.insert_one(newItem)
         return {"taskInformation": item,}
    except Exception as e:
        return {"error": str(e)}

@app.get("/getAllTasks/{limit}")
async def getAllTasks(limit:int):
    taskCollection = AppConstant.db.get_collection1()

    # Retrieve all tasks from the collection
    tasks = taskCollection.find({}).sort("createdAt",pymongo.DESCENDING).limit(limit)

    tasks_list = list(tasks)

    if len(tasks_list) == 0:
        raise HTTPException(status_code=404, detail="No tasks found")

    return {"tasks": tasks_list}

@app.delete("/deleteTask/{taskId}")
async def deleteTask(taskId:str):
        taskCollection = AppConstant.db.get_collection1()
        try:
          taskCollection.delete_one({"_id":taskId})
        except:
           raise  HTTPException(status_code=400,detail="Invalid task id")

        return {"message": "Task deleted successfully"}

@app.put("/updateTask/{taskId}")
async def updateTask(taskId: str, item: AddItem = Body(..., title="Update task in case of deletion")):
    taskCollection = AppConstant.db.get_collection1()
    updateQuery = {"$set": {"itemName": item.itemName, "isCompleted": item.isComleted, "priority": item.priority}}
    
    try:
        result = taskCollection.update_one({"_id": taskId}, updateQuery)
        print("task id is "+taskId)
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Task not found")
        else:
            return {"message": "Task updated successfully"}
    except PyMongoError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/search/{searchQuery}")
async def searchTask(searchQuery:str):
        try:
            taskCollection = AppConstant.db.get_collection1()
            searchResult=taskCollection.find({"itemName":{"$regex":searchQuery,"$options":"i"}})
            searchList=list(searchResult)
            return {"searchResult":searchList}
        except Exception as e:
            return {"error":str(e)}

        

