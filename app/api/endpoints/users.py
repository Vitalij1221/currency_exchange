from fastapi import FastAPI, Depends,HTTPException
from models.user import CreateUser

app = FastAPI()

fake_bd = []

@app.post("/register", response_model=CreateUser)
async def register_user(user: CreateUser):
    fake_bd.append({'username':user.name, 'password':user.password})
    