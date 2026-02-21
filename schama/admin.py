import datetime
from pydantic import BaseModel

Class_admin(BaseModel): 
    id: int
    name: str
    email: str
    password: str 
    created_at: datetime
    update_at: datetime