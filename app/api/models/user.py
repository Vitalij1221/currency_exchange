from pydantic import BaseModel

class CreateUser(BaseModel):
    
    password: str
    name: str