from pydantic import BaseModel,ValidationError
class UserDetail(BaseModel):
    name:str
    age:int
    language:list
class Item(BaseModel):
    name:str
    description:str 
    price:int
    userdetail:UserDetail
    