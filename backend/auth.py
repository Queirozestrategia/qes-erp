from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Login(BaseModel):
    username: str
    password: str

# usuário mock (depois vamos ligar no banco)
users = {
    "admin": "1234"
}

@router.post("/login")
def login(data: Login):
    if data.username in users and users[data.username] == data.password:
        return {"status": "ok"}
    return {"status": "erro"}