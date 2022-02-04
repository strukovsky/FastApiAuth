### FastApi with authentication project  
# Simple project shows integration of FastApi with SQLAlchemy and pydantic  

## Setup guide

Start python env

    python3 -m venv venv
    pip install -r requirements.txt

Start project
    uvicorn main:app

## Test with test shell scripts:
POST request (create new user)  
    
    curl -X 'POST' \
    -H 'Content-type: application/json' \
    -H 'accept: application/json' \
    -d '{"username": "YOUR_USER"}' localhost:8000

This endoint returns to us a token to authenticate. One should send this token in ```Authenticate``` header of GET query.
Token looks like this

    eyJ1c2VybmFtZSI6ICIkezF9IiwgInNpZ25hdHVyZSI6ICJiJ1xceGFiXFx4OGZcXHhlNFxceGJmbFxceGQyXFx4ZmVWXFx4YjlcXHg5MFxceDBiOlxceGJiclxceGU3XFx4ZWEnIn0=

GET request can be accessed with

    curl -X 'GET' -H "Authenticate: YOUR_AUTH_TOKEN" localhost:8000/
