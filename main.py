from fastapi import FastAPI, Depends
from fastapi.responses import Response
from fastapi.security import APIKeyHeader
from authenticate import authenticate, create_token
from db import Session, User
from models import User as UserApiModel
from time import time

app = FastAPI()
auth_scheme = APIKeyHeader(name="authenticate")


@app.get("/")
async def index(encoded_token: str = Depends(auth_scheme)):
    try:
        username = authenticate(encoded_token)
        return username
    except Exception as e:
        print(e)
        return Response(status_code=401)
    


@app.post("/")
async def create_user(api_user: UserApiModel,
                      ):
    username = api_user.username
    timestamp = int(time())
    user = User(username=username, timestamp=timestamp)
    session = Session()
    already_exists = session.query(User).filter(User.username==username).count() > 0
    if not already_exists:
        session.add(user)
        session.commit()
        token = create_token(username, timestamp)
        return Response(content=token)
    else:
        return Response(status_code=400, content="User already exists")



