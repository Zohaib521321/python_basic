import requests
import json
response=requests.get("https://dummyjson.com/products/1")
if(response.status_code==200):
    print("Success")
    jsonResponse=response.json()
    id=jsonResponse["id"]
    print(id)


postApiResponse=requests.post("https://dummyjson.com/auth/login",headers={ 'Content-Type': 'application/json' },
                              data=json.dumps({
                                   "username": 'kminchelle',
    "password": '0lelplR',
    "expiresInMins": 30, 

                              })
                              )    
print(postApiResponse.status_code)
print(postApiResponse.text)