from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/health_check")
def health_check():
    return "FastAPI is running properly"


users = {}

class temp2(BaseModel):
    user_no : str
    username : str
    phone_no: str
    age : int
    address : str


# adding users
@app.post("/temp1")
def temp1(dummy_data: temp2):
    users[dummy_data.user_no] = dummy_data
    return"data added"


# get all users
@app.get("/temp3")
def temp3():
    return users


# get specific users
@app.get("/temp4/{user_id}")
def temp4(user_id):
    return users[user_id]


# delete specific users
@app.get("/delete_users/{user_id}")
def delete_users(user_id):
    del users[user_id]
    return "data deleted"