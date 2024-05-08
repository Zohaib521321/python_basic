from crud import app
from constants import AppConstant

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
    AppConstant.db
    print("Welcome to pymongo")
  