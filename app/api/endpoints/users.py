from fastapi import FastAPI, Depends,HTTPException
from models.user import CreateUser
from database import fake_bd
from passlib.context import CryptContext

app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')


def hash_password(password: str) -> str:
    return pwd_context.hash(password)

@app.post("/register")
async def register_user(user: CreateUser):
    existing_user = next((u for u in fake_bd if u["email"] == user.email or u["name"] == user.name), None)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed_password = hash_password(user.password)
    
    fake_bd.append({'username':user.name, 'password':hashed_password})
    return {'message': f"Пользователь {user.username} успешно добавлен."}