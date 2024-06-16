from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="Mansoor's API",
    description="This is a sample API for learning purpose."
)

class User(BaseModel):
    id: int
    username: str
    age: int
    email: str


users = [
    {
        "id": 1,
        "username": "jhon",
        "age": 20,
        "email": "jhon@doe.com"
    },
    {
        "id": 2,
        "username": "mary",
        "age": 22,
        "email": "mary@abc.com"
    },
    {
        "id": 3,
        "username": "peter",
        "age": 31,
        "email": "peter@app.com"
    },
    {
        "id": 4,
        "username": "smith",
        "age": 29,
        "email": "black@smith.com"
    },
]


@app.get("/")
def health():
    return {"status": "ok"}


@app.get("/users", tags=["users"])
def get_all_users():
    return {"users": users, "count": len(users)}


@app.get("/users/{user_id}", tags=["users"])
def get_user(user_id: int):
    return [user for user in users if user["id"] == user_id][0]


@app.post("/users", tags=["users"])
def create_user(user: User):
    users.append(user.model_dump())
    return {
        "user": user,
        "message": "User created successfully."
    }

@app.put("/users/{user_id}", tags=["users"])
def edit_user(user_id: int, user: User):
    users[user_id - 1] = user # type: ignore
    return {"user": user, "message": "User updated successfully."}


@app.delete("/users/{user_id}", tags=["users"])
def delete_user(user_id: int):
    del users[user_id - 1]
    return "User deleted successfully."
