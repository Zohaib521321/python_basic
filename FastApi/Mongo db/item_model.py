from pydantic import BaseModel

class AddItem(BaseModel):
    itemName:str
    isComleted:bool
    priority:int

