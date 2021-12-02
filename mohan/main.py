from fastapi import Depends, FastAPI
import jwt
from typing import Optional
from fastapi.security import OAuth2PasswordBearer

users_data = {'santosh': 9251, "tarun": 1923, 'mohan': 9571}

app = FastAPI()

@app.get("/")
def read_root():
    return ({"Hii": "Sir.."})

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/login")
def read_item(user_name:str, password:str):
    if user_name in users_data:
        user = users_data[user_name]
        if str(user) == password:
            payload_data = {"user_name": user_name}
            encoded_jwt = jwt.encode(payload=payload_data, key="secreat")
            return("login success", encoded_jwt)
        else:
            return("username and password not matched")

    else:
        return("login_error")