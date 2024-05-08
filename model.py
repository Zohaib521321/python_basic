import json

class UserModel:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def fromJson(cls, jsonStr):
        data = json.loads(jsonStr)
        return cls(data["name"], data["age"])  
    
    def toJson(self):
        return json.dumps({
            'name': self.name,
            'age': self.age
        })
   
user1 = UserModel("Zohaib", 19)  
jsonInStr = user1.toJson()
print(jsonInStr)

user2 = UserModel.fromJson(jsonInStr)
print(user2.name)
