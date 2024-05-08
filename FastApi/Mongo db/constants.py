from datetime import datetime
from database import Database
import uuid
class AppConstant:
    @staticmethod
    def uniqueid()->str:
        return str(uuid.uuid4())
    db=Database()
