import os
import sys
import datetime
import json
from oop import StaticProgramm
print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])

os.getcwd()
os.name

now=datetime.datetime.now()
formattedDate=now.strftime("%Y-%m-%d %I:%M:%S %p")
print("Current date time is ",now)
print("Formatted date is", formattedDate)



data={
    "name":"Zohaib",
    "age" :18,
    "city":"Faisalabad",
    "Language":["Python","dart","C++"],
    "isStudent":True
}
json_string=json.dumps(data)

with open("data.json","w") as f:
    json.dump(data,f)
with open("data.json","r") as f:
    print(json.load(f))
StaticProgramm.greet()    
